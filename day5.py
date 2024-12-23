from useful_class import UsefulClass
import re

# Read the page ordering rules from a file. Assumes UsefulClass.read_lines_to_array returns a list of strings.
rules = UsefulClass.read_lines_to_array("assets/txt/day5pt1")
# Read the page numbers for each update from a file. Assumes UsefulClass.read_lines_to_array returns a list of strings.
prints = UsefulClass.read_lines_to_array("assets/txt/day5pt2")

def is_valid_page_order(rules, numbers):
    """
    Checks if the page order is valid based on the given rules.

    Args:
        rules: A list of strings representing the page ordering rules (e.g., "47|53").
        numbers: A list of integers representing the page numbers in an update.

    Returns:
        True if the page order is valid according to the rules, False otherwise.
    """
    seen_pages = set()  # Keep track of pages that have already been encountered in the current order check. Using a set for efficient membership checking.

    for page in numbers:
        escaped_page = re.escape(str(page))  # Escape the page number in case it contains special regex characters.
        pattern = f"\\b{escaped_page}\\|(\\d+)\\b"  # Create a regex pattern to match rules where the current page comes before another page.
                                                    # \b ensures word boundaries so "82" doesn't match "182"
                                                    # \| matches the literal "|" character.
                                                    # (\d+) captures the "other page" number.
        for rule in rules:
            match = re.search(pattern, rule)  # Search for the pattern in the current rule.
            if match:
                other_page = int(match.group(1))  # Extract the "other page" number from the capture group and convert it to an integer.
                if other_page in seen_pages:  # Check if the "other page" has already been seen.
                    return False  # If the "other page" has been seen, the order is invalid.
        seen_pages.add(page)  # Add the current page to the set of seen pages.

    return True  # If all checks pass, the page order is valid.

import re

def reorder_pages(rules, numbers):
    """
    Attempts to reorder a list of page numbers according to the given rules.

    Args:
        rules: A list of strings representing the page ordering rules (e.g., "47|53").
        numbers: A list of integers representing the page numbers to reorder.

    Returns:
        A tuple: (is_invalid, reordered_numbers)
        - is_invalid: True if the original order was invalid and could be reordered, False if the original order was valid or could not be reordered.
        - reordered_numbers: The reordered list of page numbers, or the original list if no reordering was possible/needed.
    """

    num_pages = len(numbers)
    # Create a graph representing the dependencies between pages.
    graph = {page: [] for page in numbers}
    in_degree = {page: 0 for page in numbers}

    for rule in rules:
        for page in numbers:
            escaped_page = re.escape(str(page))
            pattern = f"\\b{escaped_page}\\|(\\d+)\\b"
            match = re.search(pattern, rule)
            if match:
                other_page = int(match.group(1))
                if other_page in numbers:  # Only consider other pages that are in the input numbers
                    graph[page].append(other_page)
                    in_degree[other_page] += 1

    # Topological Sort (Kahn's Algorithm)
    queue = [page for page in numbers if in_degree[page] == 0]
    reordered_numbers = []

    while queue:
        page = queue.pop(0)
        reordered_numbers.append(page)
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(reordered_numbers) != num_pages:
        return True, numbers # Cycle detected, cant reorder
    
    if reordered_numbers == numbers:
        return False, numbers # Order was already correct

    return True, reordered_numbers  # Reordered successfully

def day5pt1():
    # Initialize the total sum of middle page numbers.
    total = 0

    # Iterate through each line representing an update's page numbers.
    for line in prints:
        numbers_str = re.split(r"\,", line)  # Split the comma-separated string of page numbers into a list of strings.
        numbers = [int(num) for num in numbers_str]  # Convert the list of string page numbers to a list of integers.
        is_valid = is_valid_page_order(rules, numbers)  # Check if the page order for the current update is valid.

        if is_valid:  # If the page order is valid:
            middle_index = int(len(numbers) / 2)  # Calculate the index of the middle page.
            total += numbers[middle_index]  # Add the middle page number to the total.

    # Print the total sum of middle page numbers from valid updates.
    print(total)

def day5pt2():
    total = 0
    for line in prints:
        numbers_str = re.split(r"\,", line)
        numbers = [int(num) for num in numbers_str]
        is_invalid, reordered_numbers = reorder_pages(rules, numbers)
        if is_invalid:
            middle_index = int(len(reordered_numbers) / 2)
            total += reordered_numbers[middle_index]

    print(total)

day5pt1()
day5pt2()