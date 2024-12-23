from useful_class import UsefulClass

# Bad
def is_safe_report(report):
    """Checks if a report is safe according to the given rules.

    Args:
        report: A list of integers representing the report levels.

    Returns:
        True if the report is safe, False otherwise.
    """

    if len(report) < 2:  # A report with less than 2 levels is considered safe
        return True

    increasing = report[1] > report[0]
    decreasing = report[1] < report[0]

    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])

        if diff < 1 or diff > 3:
            return False  # Difference outside allowed range

        if (report[i] > report[i - 1] and not increasing) or (report[i] < report[i - 1] and not decreasing):
            return False  # Inconsistent direction

    return True

def is_safe_report_pt_2(report):
    """Checks if a report is safe, allowing for one problematic number (popping)."""
    report = report[:]  # Create a copy
    if len(report) < 2:
        return True

    problem_found = False
    i = 1

    while i < len(report):
        diff = abs(report[i] - report[i - 1])
        increasing = report[i] > report[i-1]
        decreasing = report[i] < report[i-1]

        if diff < 1 or diff > 3 or (report[i] > report[i - 1] and not increasing and i!=1) or (report[i] < report[i - 1] and not decreasing and i!=1):
            if problem_found:
                return False
            else:
                report.pop(i)
                problem_found = True
                if len(report) < 2:
                    return True
                continue  # Important: Do NOT increment i after popping
        i += 1

    #Recheck the increasing/decreasing trend after the potential pop
    if len(report) >= 2:
        increasing = report[1] > report[0]
        decreasing = report[1] < report[0]
        for i in range(1, len(report)):
            if (report[i] > report[i - 1] and not increasing) or (report[i] < report[i - 1] and not decreasing):
                return False

    return True

def calculate_num_of_safe_reports(filepath, part):
    """Counts the number of safe reports in a file.

    Args:
        filepath: The path to the file containing the reports.

    Returns:
        The number of safe reports, or None if there's an error.
    """
    lines_array = UsefulClass.read_lines_to_array(filepath)

    if lines_array is None:
        return None

    num_of_safe_reports = 0

    for line in lines_array:
        try:
            report = list(map(int, line.split())) #convert to list of ints
            if part == 1:
                if is_safe_report(report):
                    num_of_safe_reports += 1
            if part == 2:
                if is_safe_report_pt_2(report):
                    # print(line)
                    num_of_safe_reports += 1
        except ValueError:
            print(f"Error: Invalid line format: {line}")
            return None

    return num_of_safe_reports

# Good
def check_sequence(sequence):
    """
    Checks if a sequence is ascending or descending with gaps of 1 to 3.

    Args:
        sequence: A list of numbers.

    Returns:
        True if the sequence passes the check, False otherwise.
    """

    n = len(sequence)
    if n <= 1:
        return True  # A sequence of 0 or 1 elements always passes

    diffs = [sequence[i+1] - sequence[i] for i in range(n - 1)]

    # Check if all diffs are within the range [-3, -1] or [1, 3] and have the same sign
    if all(-3 <= d <= -1 for d in diffs) or all(1 <= d <= 3 for d in diffs):
        return True

    return False

def check_sequence_with_removal(sequence):
    """
    Checks a sequence, allowing for removal of one number.

    Args:
        sequence: A list of numbers.

    Returns:
        True if the sequence passes the check (with or without removal), False otherwise.
    """
    if check_sequence(sequence):
        return True
    
    n = len(sequence)
    for i in range(n):
        temp_sequence = sequence[:i] + sequence[i+1:]
        if check_sequence(temp_sequence):
            return True
    return False

def calculate_num_of_safe_reports_2(filepath, part):
    """Counts the number of safe reports in a file.

    Args:
        filepath: The path to the file containing the reports.

    Returns:
        The number of safe reports, or None if there's an error.
    """
    lines_array = UsefulClass.read_lines_to_array(filepath)

    if lines_array is None:
        return None

    num_of_safe_reports = 0

    for line in lines_array:
        try:
            report = list(map(int, line.split())) #convert to list of ints
            if part == 1:
                if check_sequence(report):
                    num_of_safe_reports += 1
            if part == 2:
                if check_sequence_with_removal(report):
                    # print(line)
                    num_of_safe_reports += 1
        except ValueError:
            print(f"Error: Invalid line format: {line}")
            return None

    return num_of_safe_reports

# Wrong
# # Day 2 part 1:
# file_path_day2 = "assets/txt/day2" #change to your file path
# num_safe_day2 = calculate_num_of_safe_reports(file_path_day2, 1)
# if num_safe_day2 is not None:
#     print(f"Number of safe reports from day2 file: {num_safe_day2}")

# # Day 2 part 2:
# num_safe_day2_pt2 = calculate_num_of_safe_reports(file_path_day2, 2)
# if num_safe_day2_pt2 is not None:
#     print(f"Number of safe reports from day2 file: {num_safe_day2_pt2}")

# Day 2 part 1:
file_path_day2 = "assets/txt/day2" #change to your file path
num_safe_day2 = calculate_num_of_safe_reports_2(file_path_day2, 1)
if num_safe_day2 is not None:
    print(f"Number of safe reports from day2 file: {num_safe_day2}")

# Day 2 part 2:
num_safe_day2_pt2 = calculate_num_of_safe_reports_2(file_path_day2, 2)
if num_safe_day2_pt2 is not None:
    print(f"Number of safe reports from day2 file: {num_safe_day2_pt2}")