from collections import deque

def is_valid_move(x, y, matrix, prev_height):
    # Check bounds and if the height increases by 1
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and int(matrix[x][y]) == prev_height + 1:
        return True
    return False

def bfs(matrix, start_x, start_y):
    # BFS to count reachable 9's starting from a trailhead
    queue = deque([(start_x, start_y)])
    visited = set()
    visited.add((start_x, start_y))
    count_9s = 0
    
    while queue:
        x, y = queue.popleft()
        
        # If we reach a 9, increment the count
        if matrix[x][y] == '9':
            count_9s += 1
        
        # Try moving to neighboring cells (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid_move(nx, ny, matrix, int(matrix[x][y])):
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return count_9s

def find_distinct_trails(x, y, matrix, memo):
    # If we've already calculated the number of trails from this position, return it
    if (x, y) in memo:
        return memo[(x, y)]
    
    # Base case: If we reach a position with height 9, it's a valid trail
    if matrix[x][y] == '9':
        return 1
    
    # Initialize the count of distinct trails
    distinct_trails = 0
    
    # Try moving to neighboring cells (up, down, left, right)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, matrix, int(matrix[x][y])):
            distinct_trails += find_distinct_trails(nx, ny, matrix, memo)
    
    # Memoize the result for this position
    memo[(x, y)] = distinct_trails
    return distinct_trails

def day10pt1():
    # Load matrix map
    matrix = []
    with open("assets/txt/day10", "r") as file:
        for line in file:
            matrix.append(line.strip())
    
    total_score = 0
    
    # Iterate through the matrix to find all trailheads (0's)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == '0':
                # From this trailhead, perform BFS to count reachable 9's
                score = bfs(matrix, x, y)
                total_score += score
    
    print("Sum of the scores of all trailheads:", total_score)

def day10pt2():
    # Load matrix map
    matrix = []
    with open("assets/txt/day10", "r") as file:
        for line in file:
            matrix.append(line.strip())
    
    total_rating = 0
    memo = {}  # Dictionary to store the number of distinct trails for each position
    
    # Iterate through the matrix to find all trailheads (0's)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == '0':
                # From this trailhead, calculate the number of distinct trails
                rating = find_distinct_trails(x, y, matrix, memo)
                total_rating += rating
    
    print("Sum of the ratings of all trailheads:", total_rating)

# Run the function
day10pt1()

# Run the function for part 2
day10pt2()
