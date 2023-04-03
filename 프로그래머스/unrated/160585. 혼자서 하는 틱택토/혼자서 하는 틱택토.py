def check_win(player, board):
    # 가로 체크
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
    # 세로 체크
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # 대각선 체크
    if all(board[i][i] == player for i in range(3)):
            return True
    if all(board[i][2 - i] == player for i in range(3)):
            return True

    return False

def solution(board):
    cnt_O = sum(row.count('O') for row in board)
    cnt_X = sum(row.count('X') for row in board)
    
    if cnt_X - cnt_O > 0 or abs(cnt_X - cnt_O) > 1:
        return 0

    elif (check_win('O', board) and cnt_X != cnt_O - 1) or (check_win('X', board) and cnt_X != cnt_O):
        return 0

    return 1