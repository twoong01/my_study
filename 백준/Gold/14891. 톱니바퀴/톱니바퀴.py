from collections import deque

def rotate_right(x, d):
    if x > 4 or gear_lst[x - 1][2] == gear_lst[x][6]:
        return
    if gear_lst[x - 1][2] != gear_lst[x][6]:
        rotate_right(x + 1, -d)
        gear_lst[x].rotate(d)
def rotate_left(x, d):
    if x < 1 or gear_lst[x][2] == gear_lst[x + 1][6]:
        return
    if gear_lst[x][2] != gear_lst[x + 1][6]:
        rotate_left(x - 1, -d)
        gear_lst[x].rotate(d)


# N극 : 0, S극 : 1
gear_lst = dict()
for i in range(1, 5):
    gear_lst[i] = deque((map(int, input())))
k = int(input()) # 회전 횟수
for _ in range(k):
    num, direction = map(int, input().split())
    rotate_right(num + 1, -direction)
    rotate_left(num - 1, -direction)
    gear_lst[num].rotate(direction)

ans = 0
for i in range(4):
    ans += gear_lst[i + 1][0] * (2**i)
print(ans)