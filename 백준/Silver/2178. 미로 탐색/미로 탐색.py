# 미로 탈출
# N X M 크기의 직사각형 형태의 미로에 갇혔습니다.
# 동빈이의 위치는 (1,1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한번에
# 한 칸씩 이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로
# 표시되어있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

# 입력 조건
# 첫째 줄에 두 정수 N, M이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수로
# 미로의 정보가 주어집니다. 각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다.
# 또한 시작 칸과 마지막 칸은 항상 1입니다.

# 출력 조건
# 첫째 줄에 최소 이동 칸의 개수를 출력합니다.

# 문제 해결 아이디어
# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색합니다.
# 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일합니다.
    # 따라서 (1,1)지점부터 BFS를 수행하면 모든 노드의 최단 거리 값을 기록하면 해결할 수 있습니다.
# 예시로 3 X 3을 생각해보자

from collections import deque
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
# 이동할 방향 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maze[n -1][m - 1]

print(bfs(0,0))