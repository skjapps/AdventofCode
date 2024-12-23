import re
from useful_class import UsefulClass

def find_word_in_matrix(matrix, word):
    rows = len(matrix)  # Get the number of rows
    cols = len(matrix[0]) if rows > 0 else 0  # Get the number of columns (handle empty matrix)
    word_len = len(word)  # Get the length of the word to search
    occurrences = 0  # Initialize the count of occurrences

    for r in range(rows):  # Iterate through each row
        for c in range(cols):  # Iterate through each column
            # At each cell (r, c), check all 8 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                # dr: change in row, dc: change in column
                # (0, 1): right, (1, 0): down, (0, -1): left, (-1, 0): up
                # (1, 1): down-right, (1, -1): down-left, (-1, 1): up-right, (-1, -1): up-left

                match = True  # Assume a match until proven otherwise
                for i in range(word_len):  # Check each letter of the word
                    nr, nc = r + i * dr, c + i * dc  # Calculate the next row and column
                    # nr: new row, nc: new column
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == word[i]:
                        # If within bounds AND the letter matches
                        continue  # Keep checking
                    else:
                        match = False  # No match
                        break  # Stop checking this direction
                if match:  # If the entire word matched in this direction
                    occurrences += 1  # Increment the count

    return occurrences  # Return the total count

def rotate_matrix(matrix):
    """Rotates a matrix 90 degrees clockwise."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    rotated = [["" for _ in range(rows)] for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            rotated[c][rows - 1 - r] = matrix[r][c]
    return rotated

def find_pattern_in_matrix(matrix, pattern):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    pattern_rows = len(pattern)
    pattern_cols = len(pattern[0]) if pattern_rows > 0 else 0
    occurrences = 0

    for _ in range(4):  # Try the pattern in 4 rotations
        for r in range(rows - pattern_rows + 1):
            for c in range(cols - pattern_cols + 1):
                match = True
                for pr in range(pattern_rows):
                    for pc in range(pattern_cols):
                        if pattern[pr][pc] != "." and matrix[r + pr][c + pc] != pattern[pr][pc]:
                            match = False
                            break
                    if not match:
                        break
                if match:
                    occurrences += 1
        pattern = rotate_matrix(pattern) # Rotate for the next check
    return occurrences

# My shit solution for part 1 (misses overlaps)
def day_4_part_1(array):
    total_occurrences = 0
    # Forward Backward
    for line in array:
        # Forward
        total_occurrences += find_occurrences(line, r"XMAS")
        # Backward
        total_occurrences += find_occurrences(line, r"SAMX")

    # Left Right
    transpose_array = []
    # Filling with strings in transpose array
    for i in range(len(array[0])):
        transpose_array.append("")
    # Transposing array (?)
    for i in range(len(array[0])):
        for line in array:
            transpose_array[i] += (line[i])
    # Forward Backward on transpose = Left Right?
    for line in transpose_array:
        # Forward
        total_occurrences += find_occurrences(line, r"XMAS")
        # Backward
        total_occurrences += find_occurrences(line, r"SAMX")

    # Diagonals
    diagonals = get_diagonals(array)
    for diagonal in diagonals:
        total_occurrences += find_occurrences(diagonal, r"XMAS")
        total_occurrences += find_occurrences(diagonal, r"SAMX")

    return total_occurrences

# Day 4 Part 1:
file_path_day4 = "assets/txt/day4" 
word_to_find = "XMAS"
occurrences = find_word_in_matrix(UsefulClass.read_lines_to_array(file_path_day4), word_to_find)
print(f"Occurrences of '{word_to_find}': {occurrences}")

# Day 4 Part 2:
pattern = [
    "M.S",
    ".A.",
    "M.S"
]
occurrences = 0
# for i in range(4):
occurrences += find_pattern_in_matrix(UsefulClass.read_lines_to_array(file_path_day4), pattern)
    # pattern = rotate_matrix(pattern)
print(f"Occurrences of '{pattern}': {occurrences}")

pattern1 = [
    "M.S",
    ".A.",
    "M.S"
]

pattern2 = [
    "S.M",
    ".A.",
    "S.M"
]

pattern3 = [
    "S.S",
    ".A.",
    "M.M"
]

pattern4 = [
    "M.M",
    ".A.",
    "S.S"
]

occurrences1 = find_pattern_in_matrix(UsefulClass.read_lines_to_array(file_path_day4), pattern1)
print(f"Occurrences of pattern1: {occurrences1}")

occurrences2 = find_pattern_in_matrix(UsefulClass.read_lines_to_array(file_path_day4), pattern2)
print(f"Occurrences of pattern2: {occurrences2}")

occurrences3 = find_pattern_in_matrix(UsefulClass.read_lines_to_array(file_path_day4), pattern3)
print(f"Occurrences of pattern3: {occurrences3}")

occurrences4 = find_pattern_in_matrix(UsefulClass.read_lines_to_array(file_path_day4), pattern4)
print(f"Occurrences of pattern4: {occurrences4}")
