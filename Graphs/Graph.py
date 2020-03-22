########################################################################################################################
######################################################### Graph ########################################################


'''
A graph is a set of vertices and edges that form conections between the vertices. In a more formal approach, a graph G is
an ordered pair of a set of vertices and a set E of edges, give  = (V,E) in formal mathematical notation.

Graphs can be represented with two main forms while inplementing them in Pyton. One way is to use adjacency list
and other is to use adjacency matrix.

An adjacency list stores all the nodes, along with other nodes that are directly connceted to them in the graph.
Two nodes, A and B, in a graph g, are said to be adjacent if there is a direct connection between them. A list
data structure in Python is used to represent a graph. the indies of the list can be used to represent the nodes
or vertices in the graph.

'''

graph = dict()
graph['A'] = ['B','C']
graph['B'] = ['E', 'C', 'A']
graph['C'] = ['A','B','E','F']
graph['E'] = ['B','C']
graph['F'] = ['C']

print(graph)