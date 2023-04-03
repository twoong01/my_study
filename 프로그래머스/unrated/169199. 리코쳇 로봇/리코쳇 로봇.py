from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    answer = 0
    H = len(board)
    W = len(board[0])
    for i in range(H):
        for j in range(W):
            if board[i][j] == 'R':
                start_x = i
                start_y = j

    isvisited = [[0 for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append([start_x, start_y])
    isvisited[start_x][start_y] = 1
    while q:
        x, y = q.popleft()
        if board[x][y] == 'G':
            answer = isvisited[x][y]
            break
        for k in range(4):
            nx, ny = x, y  
            while True:
                nx += dx[k]
                ny += dy[k]
                if (0 <= nx < H and 0 <= ny < W) and board[nx][ny] == 'D':
                    nx -= dx[k]
                    ny -= dy[k]
                    break
                if not(0 <= nx < H and 0 <= ny < W):
                    nx -= dx[k]
                    ny -= dy[k]
                    break
            if not isvisited[nx][ny]:
                isvisited[nx][ny] = isvisited[x][y] + 1
                q.append([nx, ny])
    if answer > 0:
        return answer - 1
    else:
        return -1
            
            
            