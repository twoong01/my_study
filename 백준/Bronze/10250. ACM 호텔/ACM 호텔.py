from math import ceil
T = int(input())
for t in range(T):
    h, w, n = list(map(int, input().split()))
    hotel = [[0] * w for _ in range(h)]
    room_column = ceil(n / h)
    room_row = h - ((h * room_column) - n)
    if room_row == 0:
        room_number = 100 + room_column
    else:
        room_number = room_row * 100 + room_column
    print(room_number)