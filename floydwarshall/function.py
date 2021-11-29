# Recursive Version of the Floyd Warshall Algorithm with Python


def floydWarshall(dist):

    # Detect the number of vertices of the input graph
    v = len(dist)

    # Define Recursive forumla for finding
    # the shortest path between two vertices

    def shortestPath(i, j, k):

        # Return weight when there are no intermediary vertices
        # This is when k == -1 since index 0 is vertex 1
        if k == -1:
            return dist[i][j]

        # If travelling via k is shorter return shorter distance
        else:
            return min(shortestPath(i, j, k - 1),
                       shortestPath(i, k, k - 1) + shortestPath(k, j, k - 1))

    # Find shortest path and update graph
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = shortestPath(i, j, k)
    return dist
