# Challenge Log
Honestly have been using gemini 2.0 flash experimental for everything its well smart

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

## Day 1:
Cheated mostly, but it wasn't too crazy
- mapping to multiple variables with implicit type change to int
- 

## Day 2:

## Day 4:
Actually hard lol a matrix implementation for finding not just words but some fucking crazy patterns... 

## Day 5:
### Pt 2:
Key Changes and Explanations:

Graph Representation: The code now uses a dictionary graph to represent the dependencies between pages. graph[page] stores a list of pages that must come after page. in_degree stores the number of pages that must come before a given page.
Topological Sort (Kahn's Algorithm): The core of the reordering is now a topological sort algorithm. This algorithm is designed to order nodes in a directed graph (like our page dependencies) such that for every directed edge from node A to node B, node A appears before node B in the ordering.
Cycle Detection: If the topological sort doesn't produce an ordering of all the input pages (i.e. if len(reordered_numbers) != len(numbers)), it means there's a cycle in the dependencies (an impossible ordering), and the function returns the original list and True to indicate its invalid and can't be reordered.
Already Correct: if the reordered list and the original list are the same then it returns the original list and False to indicate it was already correct.
Clearer Return Value: The function now returns a tuple (is_invalid, reordered_numbers). This makes it clear whether reordering was necessary/possible and provides the reordered list.
Corrected Main Loop: The main loop uses the correct tuple unpacking and uses the reordered list if the order was invalid.
Only consider numbers in input: The code now only adds other pages to the graph if they are actually in the input numbers, this prevents errors if a rule refers to a page that isn't in the current update.
This implementation now correctly reorders the pages according to the rules, detects impossible orderings (cycles), and provides a clear way for the main code to use the reordered list.






wow this is pretty intense, i thought just finding a rule and reordering would be simple



You're right, it might seem like a simple "find and swap" operation at first glance, but the problem has a subtle complexity that requires a more robust approach like topological sorting. Here's why a simple reordering based on individual rules isn't sufficient:

Why Simple Reordering Doesn't Work:

Consider this simplified example:

Rules:

A|B
B|C
C|A
Pages:

C, B, A
If you try to reorder based on individual rules:

Seeing "A|B", you might swap A and B: B, C, A.
Seeing "B|C", you might swap B and C: C, B, A (no change in this case).
Seeing "C|A", you might swap C and A: A, B, C.
But now, you've violated the "A|B" rule again! This creates a cycle, and no amount of simple swapping will produce a valid order.

Why Topological Sort Is Necessary:

Topological sort is designed specifically to handle these kinds of dependencies and detect cycles. Here's how it addresses the issues:

Dependency Graph: It represents the rules as a directed graph, where an edge from A to B means "A must come before B". This gives a clear visualization of the dependencies.
Cycle Detection: The algorithm inherently detects cycles. If a cycle exists (like in the A, B, C example above), it won't be able to produce a complete ordering.
Correct Ordering: If no cycles exist, the topological sort produces an ordering that respects all dependencies.
Analogy:

Imagine you have a set of tasks to complete, and some tasks have dependencies. For example:

Task A must be done before Task B.
Task B must be done before Task C.
Task C must be done before Task D.
A simple reordering might get you into trouble if you have a more complex dependency like:

Task A must be done before Task B.
Task B must be done before Task C.
Task C must be done before Task A.
This is a circular dependency. You can't complete all tasks in a way that respects all dependencies. Topological sort will detect this cycle.

In the page ordering problem, the pages are the "tasks," and the rules are the "dependencies." Topological sort is the correct tool to find a valid printing order (if one exists) and to detect cases where no valid order is possible.

So, while it seems more complex than a simple reordering, topological sort is necessary to correctly handle the dependencies and cycles inherent in the problem.


## Day 10:
### Pt 1:
To solve this challenge, you need to traverse the matrix map and find all trailheads (positions with height 0). From each trailhead, you'll need to explore the possible paths that increase by exactly 1 in height, and count how many 9s are reachable.

Here’s a Python example that can help you achieve this:

Explanation:
We start by reading the map and storing it in a 2D list (matrix).
We look for all trailheads, which are positions with height 0.
From each trailhead, we perform a depth-first search (DFS) or breadth-first search (BFS) to explore all reachable positions that follow the uphill slope condition (height increases by exactly 1).
For each trailhead, we count how many 9s are reachable and store the score.
Finally, sum the scores of all trailheads.

Key Concepts:
BFS (Breadth-First Search) is used here to explore all reachable 9s from each trailhead. You can also use DFS if you'd like.
is_valid_move function checks whether moving from one cell to an adjacent cell is valid (i.e., the height increases by exactly 1).
Queue and visited set help in managing the exploration and preventing revisiting the same cell.
Summing the scores after calculating the reachable 9s for each trailhead.
Usage:
You need to provide the file assets/txt/day10 containing the topographic map as input for this code.
The program reads the matrix, looks for trailheads (0), and calculates how many 9s can be reached from each trailhead using BFS.
Finally, the total score (sum of scores of all trailheads) is printed.
This code assumes that the map is well-formed (i.e., all rows have the same length). Let me know if you need further clarification or additional modifications!

### Pt 2:
To solve part 2 of the challenge, the goal is to determine the rating of each trailhead. The rating of a trailhead is the number of distinct hiking trails that start at that position.

Plan:
Trailhead Identification: As before, we need to identify all trailheads (positions with height 0).

Distinct Trails: To determine the number of distinct trails, we can:

Explore all possible paths from a trailhead. Every path should strictly follow the uphill slope condition (height increases by exactly 1 at each step).
Use a recursive search, backtracking, or BFS/DFS to explore all possible paths starting from a trailhead.
Memoization: To avoid redundant calculations and improve performance, we can use memoization (caching results) to store the number of distinct trails starting from each position. This prevents recalculating the number of trails for the same position multiple times.

Counting the Trails: For each trailhead, we'll calculate how many distinct trails can be formed from that position by recursively exploring all valid moves that increase the height by exactly 1.

Summing Ratings: After calculating the ratings (number of distinct trails) for each trailhead, we sum them up.

Key Points:
Memoization (memo):

We store the result of find_distinct_trails(x, y, matrix, memo) for each position (x, y) in a memo dictionary. This avoids recalculating the number of trails from the same position multiple times.
Base Case:

When we reach a position with height 9, we return 1 since it's a valid endpoint for a trail.
Exploring Directions:

We check four directions: up, down, left, and right. Only move to positions where the height increases by exactly 1.
Counting Distinct Trails:

For each trailhead, we use the find_distinct_trails function to count all possible distinct trails starting from that trailhead. The result is added to the total sum of ratings.
Example Workflow:
For each 0 (trailhead), we call find_distinct_trails(x, y, matrix, memo) to get the number of distinct trails.
Each call explores all paths from (x, y) where height increases by exactly 1, counts the distinct trails, and stores the result in memo.
Finally, we sum all the ratings and print the result.
Efficiency Considerations:
The memoization technique ensures that we don't recompute the number of trails for the same positions multiple times, which helps in reducing unnecessary recalculations and improving the performance.
The time complexity of this approach is greatly reduced due to memoization, especially when there are many overlapping subproblems in the matrix.
Next Steps:
Test the code with your topographic map to verify that it correctly computes the sum of the trailhead ratings.
Adjust file input/output as necessary, depending on how the map is stored or provided.
Let me know if you need further explanations or help with testing!