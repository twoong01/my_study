from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 방향을 나타내는 배열
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 시작 위치
    start = (0, 0)
    
    # BFS를 위한 큐
    queue = deque()
    queue.append((start, 1))  # 시작 위치와 이동 횟수를 함께 저장
    
    while queue:
        (x, y), steps = queue.popleft()
        
        # 상대 팀 진영에 도착한 경우, 이동 횟수 반환
        if x == n - 1 and y == m - 1:
            return steps
        
        for i in range(4):  # 상하좌우로 이동을 시도
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이동 가능한 위치이면 큐에 추가하고 해당 위치를 벽으로 변경 (방문 처리)
                queue.append(((nx, ny), steps + 1))
                maps[nx][ny] = 0
                
    # 상대 팀 진영에 도착하지 못한 경우
    return -1