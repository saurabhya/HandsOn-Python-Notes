'''
A graph trversal means to visit all the vertices of the graph, while keeping track of of which nodes or vertices have
already been visited and which one have not. A graph trversal algorithm is efficient if it traverse all the nodes of
the graph in the minimal possible time.

We have two graph traversal algorithms:
1. breadth first search (BFS)
2. depth first-search (DFS)

'''

######################################################################################################################
# Breadt first search (BFS)

graph = dict()
graph['A'] = ['B','G','D']
graph['B'] = ['A','F','E']
graph['C'] = ['F','H']
graph['D'] = ['F','A']
graph['E'] = ['B','G']
graph['F'] = ['B','D','C']
graph['G'] = ['A','E']
graph['H'] = ['C']

from collections import deque

def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue)>0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]

        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
    return visited_vertices

print(breadth_first_search(graph, 'A'))

'''
In the worst case scenario, each vertex or node and the edge will be traversed, thus the time complexity of
the BFS algorithm is O(|V|+|E|), where |V| is the number of vertices or nodes, while |E| is the number of edges in the graph.

'''

#########################################################################################################################################
# Depth First Seacrh(DFS)
'''
As the name suggests, the DFS algorithm traverses the depth of any particular path in the graph before traversing its breadth.
As such, child nodes are visited first before sibling nodes. The stack data structure is used to implement the DFS algorithm.
'''

def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()
    graph_stack.append(root)
    node = root

    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
                continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node
    
    return visited_vertices

print(depth_first_search(graph,'A'))