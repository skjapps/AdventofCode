import re
from useful_class import UsefulClass

def find_multiplications(text):
    """Finds all instances of "mul(number,number)" in a string.

    Args:
        text: The input string to search.

    Returns:
        A list of strings, where each string is a matched "mul(number,number)" expression.
        Returns an empty list if no matches are found.
    """
    pattern = r"mul\((\d+),(\d+)\)"  # Regex pattern
    matches = re.findall(pattern, text)
    if matches:
        full_matches = [f"mul({match[0]},{match[1]})" for match in matches]
        return full_matches
    return

def find_expressions(text):
    """Finds all instances of "mul(number,number)", "do()", and "dont()" in a string.

    Args:
        text: The input string to search.

    Returns:
        A list of strings, where each string is a matched expression.
        Returns an empty list if no matches are found.
    """
    pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, text)
    if matches:
        full_matches = []
        for match in matches:
            if match[0]: #mul match
                full_matches.append(match[0])
            elif match[1] == "" and match[2] == "": #do match
                full_matches.append(match[3])
            elif match[1] == "" and match[2] == "": #don't match
                full_matches.append(match[3])
        return full_matches
    return []

    
def do_multiplications(array):
    """Calculates the sum of multiplications, handling "do()" and "don't()".

    Args:
        array: An array of strings containing expressions.

    Returns:
        The integer sum of multiplications, or -1 on error.
    """
    total_sum = 0
    do_enabled = True  # Start with multiplications enabled

    for expression_str in array:
        if expression_str == "don't()":
            do_enabled = False
        elif expression_str == "do()":
            do_enabled = True
        elif do_enabled:  # Only perform multiplication if enabled
            try:
                match = re.match(r"mul\((\d+),(\d+)\)", expression_str)
                if match:
                    num1 = int(match.group(1))
                    num2 = int(match.group(2))
                    total_sum += num1 * num2
                else:
                    return -1  # Invalid multiplication format
            except (ValueError, AttributeError):
                return -1  # Indicate failure
    return total_sum

# Day 3 Part 1:
file_path_day3 = "assets/txt/day3" 
day3part1 = do_multiplications(find_multiplications(UsefulClass.read_lines_to_string(file_path_day3)))
print(day3part1)

print(find_expressions(UsefulClass.read_lines_to_string(file_path_day3)))
day3part2 = do_multiplications(find_expressions(UsefulClass.read_lines_to_string(file_path_day3)))
print(day3part2)
