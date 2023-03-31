import sys
input = sys.stdin.readline
# depth : 재료를 고른 개수
# idx : 인덱스
def dfs(depth, idx):
    global ans
    if depth == n // 2: # 재료를 고른 개수가 전체 재료의 개수의 절반 일 때
        food1, food2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]: # 선택한 재료일 때의 합
                    food1 += Map[i][j]
                elif not visited[i] and not visited[j]: # 선택하지 않은 다른 재료들의 합
                    food2 += Map[i][j]
        ans = min(ans, abs(food1 - food2))
        return
    
    for i in range(idx, n):
        if not visited[i]: # 사용하지 않은 재료라면
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
visited = [False for _ in range(n)]
dfs(0, 0)
print(ans)