from collections import Counter
from functools import reduce

def R(arr):
    mx = 0
    for i in range(len(arr)):
        tmp = Counter(arr[i])
        del tmp[0]
        tmp = list(tmp.items())
        tmp.sort(key=lambda x: (x[1], x[0]))
        if len(tmp) > 50: tmp = tmp[:50]
        arr[i] = reduce(lambda x, y: list(x) + list(y), tmp[1:], list(tmp[0]))

        mx = max(mx, len(arr[i]))
    for i in range(len(arr)):
        if len(arr[i]) < mx:
            arr[i].extend([0] * (mx - len(arr[i])))


def main():
    r, c, k = map(int, input().split())
    r, c = r - 1, c - 1
    Map = [list(map(int, input().split())) for _ in range(3)]
    time = 0
    if r < len(Map) and c < len(Map[0]):
        if Map[r][c] == k:
            return time
    while True:
        if len(Map) >= len(Map[0]):
            R(Map)
        else:
            Map = list(map(list, zip(*Map)))
            R(Map)
            Map = list(map(list, zip(*Map)))
        time += 1
        if time > 100: return -1
        if r < len(Map) and c < len(Map[0]):
            if Map[r][c] == k:
                return time
print(main())