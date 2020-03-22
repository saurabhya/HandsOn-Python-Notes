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

'''
Now we can esily establish that the A vertex has the adjacent vertices of B and C. The F vertex has the C vertex as
its only neighbor. Similarly, the B vertex has adjacent vertices of E, B and A.
'''

'''
ADJACENCY MATRICES

Another approach by which a graph can e repesented is by using adjacency matrix. A mtrix is a two dimensional array.
The idea here is to represent the cells with 1 or 0, depending on whether two vertices are connected by an edge or not.

An adjacency matrix can be implemented using a given adjacency list. To implement the adjacency matrix, let's take the
previous dictionary based implementation of graph.
Firstly, we obtain the key elements of the adjacency matrix. We can get the key elements by sorting the keys of the graph.

'''
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []

# The multidimensional array is filled using a nested for loop
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))

print(edges_list)

'''
The next step in implementig the adjacency matrix is to fill it, using 1 to denote the presence of an edge in the graph.
This can be done with adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1
'''
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

print(adjacency_matrix)