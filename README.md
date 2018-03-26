# PyFordFulkerson
The repository will hold a python implementation of the Ford-Fulkerson algorithm to compute the maximal flow through a graph.

The method FordFulkerson in FordFulkerson.py takes a numpy array (which is assumed to be symmetric with 0s on the diagonal, need to test this explicitly in future version), and returns a number. The ijth element of the array is interpreted as the capacity of the edge between the ith and jth vertices in a weigted undirected graph. As for this problem we only care about the total weight between vertices i and j, we take there to be a single edge between them carrying that total weight. 

The function produces a maximal flow through the graph, given the capacities, represent by the array Flow. Flow[i,j] represents the flow from vertex i to vertex j, and as such Flow should be an antisymmetric matrix (this also should be checked, though it should be enforced in the construction and manipulation of Flow). Once the maximal flow is found, the total flow through the graph is computed as the sum of the outgoing flows from the source.

The source is assumed to be the first vertex, and the sink assumed to be the last. Later we should add functions to fix this when it isn't true.

## Useful references:

* Wikipedia: [Ford-Fulkerson Algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)
* Wikipedia: [Edmonds-Karp Algorithm](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm)
