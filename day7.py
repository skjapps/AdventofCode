from useful_class import UsefulClass
import re
import itertools

def concatenate_numbers(a, b):
    return int(str(a) + str(b))

def day_7_part_1(array):
    total = 0
    for line in array:
        pattern = r"\d+"  # Simplified pattern
        numbers = [int(x) for x in re.findall(pattern, line)]

        if not numbers or len(numbers) < 2:  # Handle empty or single-number lines
            continue

        target = numbers[0]
        operands = numbers[1:]
        num_count = len(operands)

        found_match = False  # Flag to track if a match was found for the current line
        for ops in itertools.product(['+', '*', '##'], repeat=num_count - 1): #added ## as the concat operator
            result = operands[0]
            for i in range(num_count - 1):
                if ops[i] == '+':
                    result += operands[i + 1]
                elif ops[i] == '*':
                    result *= operands[i + 1]
                elif ops[i] == '##':  # Concatenation
                    result = concatenate_numbers(result, operands[i + 1])


            if result == target:
                found_match = True  # Set the flag
                break # Exit the loop as we found a match

        if found_match:  # Only add to the total if a match was found
            total += target

    return total

# Day 7 Part 1:
file_path_day7 = "assets/txt/day7" 
day7part1 = day_7_part_1(UsefulClass.read_lines_to_array(file_path_day7))
print(day7part1)