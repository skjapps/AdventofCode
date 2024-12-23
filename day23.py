from itertools import combinations
import threading
from useful_class import UsefulClass

def day23pt1(network_map):
    # Parse the network map into a dictionary of connections
    connections = {}
    for connection in network_map:
        a, b = connection.split('-')
        if a not in connections:
            connections[a] = set()
        if b not in connections:
            connections[b] = set()
        connections[a].add(b)
        connections[b].add(a)

    # Find all sets of three inter-connected computers
    sets_of_three = []
    for a, b, c in combinations(connections.keys(), 3):
        if b in connections[a] and c in connections[a] and c in connections[b]:
            sets_of_three.append({a, b, c})

    # Filter sets to include only those with at least one computer starting with 't'
    filtered_sets = [s for s in sets_of_three if any(computer.startswith('t') for computer in s)]

    # Print the results
    print(f"Total sets of three inter-connected computers: {len(sets_of_three)}")
    print(f"Sets containing at least one computer starting with 't': {len(filtered_sets)}")

def day23pt2(network_map):
    # Parse the network map into a dictionary of connections
    connections = {}
    for connection in network_map:
        a, b = connection.split('-')
        if a not in connections:
            connections[a] = set()
        if b not in connections:
            connections[b] = set()
        connections[a].add(b)
        connections[b].add(a)

    # Function to check if a set of computers is fully connected
    def is_clique(clique, connections, result):
        if all(connections[a].issuperset(clique) for a in clique):
            result.append(set(clique))

    # Function to find the largest set of fully connected computers (clique)
    def find_largest_clique(connections):
        max_clique = set()
        result = []
        threads = []
        for size in range(len(connections), 2, -1):
            for clique in combinations(connections.keys(), size):
                thread = threading.Thread(target=is_clique, args=(clique, connections, result))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
            if result:
                return result[0]
        return max_clique

    # Find the largest clique
    largest_clique = find_largest_clique(connections)

    # Generate the password by sorting the names alphabetically and joining them with commas
    password = ','.join(sorted(largest_clique))

    # Print the password
    print(f"The password to get into the LAN party is: {password}")

# Define the network map as a list of connections
network_map = UsefulClass.read_lines_to_array("assets/txt/day23")

day23pt1(network_map)

day23pt2(network_map)