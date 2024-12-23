from useful_class import UsefulClass
import re
import time

def day23pt1():
    connections = UsefulClass.read_lines_to_array("assets/txt/day23")
    connections_with_chief_computer = []
    for connection in connections:
        computer1, computer2 = map(str, re.split(r"-", connection))
        if re.match(r"^t", computer1) or re.match(r"^t", computer2):
            connections_with_chief_computer.append(connection)
    # print(connections_with_chief_computer)
    one_ways = []
    counter = 0
    for connection in connections_with_chief_computer:
        # one_ways.append([])
        computer1, computer2 = map(str, re.split(r"-", connection))
        for test_connections in connections_with_chief_computer:
            computer1test, computer2test = map(str, re.split(r"-", test_connections))
            # Same Connection
            if computer1 == computer1test and computer2 == computer2test:
                pass
            # A link between one computer
            elif (computer1 == computer1test and computer2 != computer2test):
                one_way = computer2+","+computer1+","+computer1test
                # one_ways[counter].append(one_way)
                one_ways.append(one_way)
            elif (computer1 != computer1test and computer2 == computer2test):
                one_way = computer1+","+computer2+","+computer1test
                # one_ways[counter].append(one_way)
                one_ways.append(one_way)
            else:
                pass
        # counter += 1
    # print(one_ways)
    # Pruning useless ones...?
    one_ways_pruned = []
    for one_way in one_ways:
        computer1, computer2, computer3 = map(str, re.split(",", one_way))
        if computer1 == computer2 or computer2 == computer3 or computer3 == computer1:
            pass
        else:
            one_ways_pruned.append(one_way)
    # print(one_ways_pruned)
    # Find full loops...
    full_loops = []
    for one_way in one_ways_pruned:
        computer1, computer2, computer3 = map(str, re.split(",", one_way))
        for connection in connections:
            connection1, connection2 = map(str, re.split("-", connection))
            # If the edge computers are linked
            if (computer1 == connection1 and computer3 == connection2) \
                or (computer1 == connection2 and computer3 == connection1):
                    full_loops.append(one_way)
    print(full_loops)
    print(len(full_loops))



day23pt1()