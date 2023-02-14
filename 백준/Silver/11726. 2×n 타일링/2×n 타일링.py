n = int(input())
arr = [0] * (n + 1)

def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if arr[n]:
        return arr[n]
    else:
        arr[n] = paper(n - 1) + paper(n - 2)
        return arr[n]
print(paper(n) % 10007)