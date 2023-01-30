n, m = map(int, input().split())
n_lst, m_lst = [], []
for i in range(n):
    n_lst.append(input())
for i in range(m):
    m_lst.append(input())
ans = sorted(list(set(m_lst) & set(n_lst)))
print(len(ans))
for i in ans:
    print(i)