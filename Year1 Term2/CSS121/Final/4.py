def longestPath(edges, numNodes, startNode):
    dist = [-float("Inf")] * (numNodes + 1)
    dist[startNode] = 0

    for i in range(1, numNodes + 1):
        for (node, neighbour, weight) in edges:
            if dist[node] != float("Inf") and dist[node] + weight > dist[neighbour]:
                dist[neighbour] = dist[node] + weight
    return dist
