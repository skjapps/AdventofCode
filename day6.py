from useful_class import UsefulClass

def day6pt1(matrix):
    """Simulates guard movement and counts positions visited."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    movements = 0

    while True:
        moved = False
        for y in range(rows):
            for x in range(cols):
                if matrix[y][x] in "^V<>":
                    direction = matrix[y][x]
                    new_x, new_y = x, y

                    if direction == "^":
                        new_y -= 1
                    elif direction == "V":
                        new_y += 1
                    elif direction == ">":
                        new_x += 1
                    elif direction == "<":
                        new_x -= 1

                    if not (0 <= new_x < cols and 0 <= new_y < rows):
                        # Out of bounds, stop moving this guard
                        matrix[y][x] = "X" # Mark the old position
                        moved = True
                        break  # Break the inner loop (x)
                    elif matrix[new_y][new_x] == "#":
                        # Turn right if hitting a wall
                        if direction == "^":
                            matrix[y][x] = ">"
                        elif direction == ">":
                            matrix[y][x] = "V"
                        elif direction == "V":
                            matrix[y][x] = "<"
                        elif direction == "<":
                            matrix[y][x] = "^"
                        moved = True
                        break # Break the inner loop (x)
                    else:
                        matrix[new_y][new_x] = direction
                        matrix[y][x] = "X"
                        movements += 1
                        moved = True
                        break  # Break the inner loop (x)
            if moved:
                break # Break the outer loop (y)

        if not moved:
            break

    # Write the final matrix to a file
    unique_positions = 0
    with open("assets/txt/day6pt1ans.txt", "w") as f:
        for y in range(rows):
            for x in range(cols):
                f.write(matrix[y][x])
                if matrix[y][x] == "X":
                    unique_positions += 1
            f.write("\n")

    print("Movements:", movements)
    print("Unique Positions:", unique_positions)

def find_trap_positions(matrix):
    """Find positions where an extra # traps the guards in a loop."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    def simulate(matrix, guards):
        """Simulates the guards' movement and detects loops."""
        visited_states = set()
        steps = 0

        while guards:
            new_guards = []
            for x, y, direction in guards:
                if (x, y, direction) in visited_states:
                    return True  # Loop detected
                visited_states.add((x, y, direction))

                new_x, new_y = x, y
                if direction == "^":
                    new_y -= 1
                elif direction == "V":
                    new_y += 1
                elif direction == ">":
                    new_x += 1
                elif direction == "<":
                    new_x -= 1

                if not (0 <= new_x < cols and 0 <= new_y < rows) or matrix[new_y][new_x] == "X":
                    continue  # Out of bounds or visited
                if matrix[new_y][new_x] == "#":
                    # Turn right
                    if direction == "^":
                        direction = ">"
                    elif direction == ">":
                        direction = "V"
                    elif direction == "V":
                        direction = "<"
                    elif direction == "<":
                        direction = "^"
                else:
                    # Move forward
                    x, y = new_x, new_y
                new_guards.append((x, y, direction))

            guards = new_guards
            steps += 1
            if steps > rows * cols:
                return True  # Failsafe for infinite loops

        return False

    # Identify initial guard positions and directions
    guards = []
    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] in "^V<>":
                guards.append((x, y, matrix[y][x]))

    # Test each empty cell for trap placement
    trap_positions = 0
    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] == ".":
                # Place a temporary trap
                matrix[y][x] = "#"
                if simulate([row[:] for row in matrix], guards):
                    trap_positions += 1
                # Remove the temporary trap
                matrix[y][x] = "."

    return trap_positions

# Read the matrix.
matrix_str = UsefulClass.read_lines_to_array("assets/txt/day6")
matrix = [list(line) for line in matrix_str]
print(matrix)

day6pt1(matrix)

print(find_trap_positions(matrix))
