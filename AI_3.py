def prim(adjacency_list):
    n = len(adjacency_list)
    visited = [False] * n
    mst_weight = 0
    mst_edges = []

    def find_min_edge():
        min_weight = 9999
        min_edge = None
        for i in range(n):
            if visited[i]:
                for j, weight in adjacency_list[i].items():
                    if not visited[j] and weight < min_weight:
                        min_weight = weight
                        min_edge = (i, j, weight)
        return min_edge

    visited[0] = True

    for i in range(n - 1):  
        min_edge = find_min_edge()
        if min_edge is None:
            break
        mst_edges.append(min_edge)
        mst_weight += min_edge[2]
        visited[min_edge[1]] = True

    print("\nMST Weight:", mst_weight)
    print("MST Edges:")
    for i in mst_edges:    
        print(i)


# -------- SIMPLE INPUT --------
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

adjacency_list = [{} for i in range(n)]   

print("Enter edges (u v weight):")
for i in range(e):  
    u, v, w = map(int, input().split())
    
    # Undirected graph
    adjacency_list[u][v] = w
    adjacency_list[v][u] = w

prim(adjacency_list)