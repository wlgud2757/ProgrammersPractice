def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    count = 0
    visited = [False] * n
    
    for vertex in range(n):
        if not visited[vertex]:
            dfs(vertex)
            count += 1
    
    return count
