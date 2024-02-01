def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(i, visited, n, computers)
            answer += 1
    return answer

def dfs(i, visited, n, computers):
    visited[i] = True
    for j in range(n):
        if i != j and computers[i][j]:
            if not visited[j]:
                dfs(j, visited, n, computers)
    