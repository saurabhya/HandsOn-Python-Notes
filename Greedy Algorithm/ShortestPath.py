'''
    The shortest path problem requires us to find out the shortest possible route between nodes in a graph.
    It has important applications for mapping and route planning, when plotting the most efficient way to get from point A to point B.

    Dijkstra's Algorithm is a very popular method of solving this problem. This algorithm is used to find the shortest distance
    from a source to all other nodes or vertices ina graph. Here we explain how we canuse the greedy approach to solve this problem.

    Dijkstra's algorithm works for weighted directed and undirected graphs. The algorithm produces the output of a list of the
    shortest path from a given source node A in a weighted graph. The algorithm works as follows:
    1. Initially, mark all the nodes as visited, and set their distance from the given source node to infinity(the source node is set to 0).
    2. Set the source node as current.
    3. For the current node, look for all the unvisited adjacent nodes; compute the distance to that node from the source node through
       the current node. Compare the newly computed distance to the currently assigned distance, and if it is smaller, set this as the new value.
    4. Once we have cosidered al lthe unvisited adjacent nodes of the current node, we mark it as visited.
    5. We next consider the next unvisited node which has the shortest distance from the source node. Repeat steps 2 to 4.
    6. We stop when the list of unvisited nodes is empty, meaning wee have considered all the unvisited nodes.
'''

# to represent the graph we are going to use a dictionary

graph = dict()
graph['A'] = {'B':5, 'D':9,'E':2}
graph['B'] = {'A':5, 'C':2}
graph['C'] = {'B':2, 'D':3}
graph['D'] = {'A':9, 'F':2, 'C':3}
graph['E'] = {'A':2, 'F':3}
graph['F'] = {'E':3, 'D':2}

#######################################################################################################################################
'''
    To implement Dijkstra's algorithm to find the shortest path, we begin the program for finding the shortest path, we begin the program
    for finding shotest path by representing the table that enables us to track the changes in our graph.
'''
table = dict()
table = {
    'A': [0, None],
    'B': [float("inf"), None],
    'C': [float("inf"), None],
    'D': [float("inf"), None],
    'E': [float("inf"), None],
    'F': [float("inf"), None]
}

DISTANCE = 0
PREVIOUS_NODE = 1
INFINITY = float('inf')

def find_shortest_path(graph, table, origin):
    visited_nodes = []
    current_node =  origin
    starting_node = origin
    while True:
        adjacent_nodes = graph[current_node]
        if set(adjacent_nodes).issubset(set(visited_nodes)):
            pass
        else:
            unvisited_nodes = set(adjacent_nodes).difference(set(visited_nodes))
            for vertex in unvisited_nodes:
                distance_from_starting_node = get_shortest_distance(table, vertex)
                if distance_from_starting_node == INFINITY and current_node == starting_node:
                    total_distance = get_distance(graph, vertex, current_node)
                else:
                    total_distance = get_shortest_distance(table, current_node) + get_distance(graph, current_node, vertex)
                    if total_distance < distance_from_starting_node:
                        set_shortest_distance(table, vertex, total_distance)
                        set_previous_node(table, vertex, current_node)

        visited_nodes.append(current_node)
        if len(visited_nodes)== len(table.keys()):
            break
        current_node = get_next_node(table, visited_nodes)
    return table

def get_shortest_distance(table, vertex):
    shortest_distance = table[vertex][DISTANCE]
    return shortest_distance

def set_shortest_distance(table, vertex, new_distance):
    table[vertex][DISTANCE] = new_distance

def set_previous_node(table, vertex, previous_node):
    table[vertex][PREVIOUS_NODE] = previous_node

def get_distance(graph, first_vertex, second_vertex):
    return graph[first_vertex][second_vertex]

def get_next_node(table, visited_nodes):
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes)))
    assumed_min = table[unvisited_nodes[0]][DISTANCE]
    min_vertex = unvisited_nodes[0]
    for node in unvisited_nodes:
        if table[node][DISTANCE] < assumed_min:
            assumed_min = tabe[node][DISTANCE]
            min_vertex = node
    return min_vertex

shortest_distance_table = find_shortest_path(graph, table, 'A')
for k in sorted(shortest_distance_table):
    print("{} - {}".format(k, shortest_distance_table[k]))