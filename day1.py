from useful_class import UsefulClass

def calculate_total_distance(filepath):
    """Calculates the total distance between two lists of numbers in a file.

    Args:
        filepath: The path to the file containing the number pairs.

    Returns:
        The total distance, or None if there's an error.
    """
    lines_array = UsefulClass.read_lines_to_array(filepath)
    if lines_array is None:
        return None

    left_numbers = []
    right_numbers = []

    for line in lines_array:
        try:
            num1, num2 = map(int, line.split()) #convert to int directly
            left_numbers.append(num1)
            right_numbers.append(num2)
        except ValueError:
            print(f"Error: Invalid line format: {line}")
            return None

    left_numbers.sort()
    right_numbers.sort()

    total_distance = 0
    for i in range(len(left_numbers)):
        total_distance += abs(left_numbers[i] - right_numbers[i])

    return total_distance

def calculate_similarity_score(filepath):
    """Calculates the similarity between two lists of numbers in a file.

    Args:
        filepath: The path to the file containing the number pairs.

    Returns:
        The similarity number, or None if there's an error.
    """
    lines_array = UsefulClass.read_lines_to_array(filepath)
    if lines_array is None:
        return None

    left_numbers = []
    right_numbers = []

    for line in lines_array:
        try:
            num1, num2 = map(int, line.split()) #convert to int directly
            left_numbers.append(num1)
            right_numbers.append(num2)
        except ValueError:
            print(f"Error: Invalid line format: {line}")
            return None

    left_numbers.sort()
    right_numbers.sort()

    similarity_score = 0
    for number in left_numbers:
        similarity_score += number * right_numbers.count(number)

    return similarity_score

file_path = "assets/txt/day1"

# Day 1 part 1:
total_distance = calculate_total_distance(file_path)

if total_distance is not None:
    print(f"Total distance: {total_distance}")

# Day 1 part 2:
similarity_score = calculate_similarity_score(file_path)

if similarity_score is not None:
    print(f"Similarity Score: {similarity_score}")
