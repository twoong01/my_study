def check(lst):
    for i in range(1, n):
      if abs(lst[i] - lst[i - 1]) > 1:
          return False
      if lst[i] < lst[i - 1]:
          for j in range(l):
              if i + j >= n or lst[i] != lst[i + j] or is_visited[i + j]:
                  return False
              if lst[i] == lst[i + j]:
                  is_visited[i + j] = True
      elif lst[i] > lst[i - 1]:    
          for j in range(l):
              if i - j - 1 < 0 or lst[i - 1] != lst[i - j - 1] or is_visited[i - j - 1]:
                  return False
              if lst[i - 1] == lst[i - j - 1]:
                  is_visited[i - j - 1] = True
    return True


n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    is_visited = [False for _ in range(n)]
    if check([maps[i][j] for j in range(n)]):
        cnt += 1

for i in range(n):
    is_visited = [False for _ in range(n)]
    if check([maps[j][i] for j in range(n)]):
        cnt += 1
print(cnt)