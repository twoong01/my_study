n, m = map(int, input().split())
n_lst = []
for i in range(1, n + 1):
    if n % i == 0:
        n_lst.append(i)
m_lst = []
for i in range(1, m + 1):
    if m % i == 0:
        m_lst.append(i)
ans_1 = []
for i in n_lst:
    if i in m_lst:
        ans_1.append(i)
print(max(ans_1))
n_mul = []
m_mul = [] 
for i in range(1, max(n, m) + 1):
    n_mul.append(i * n)
    m_mul.append(i * m)

for i in n_mul:
    if i in m_mul:
        print(i)
        break