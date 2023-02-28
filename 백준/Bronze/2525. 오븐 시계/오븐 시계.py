h, m = map(int, input().split())
ct = int(input())

m_1 = (m+ct)%60
h_1 = h + (m+ct)//60
if h_1 >= 24:
    h = h_1 - 24
    print(h ,m_1)
else:
    print(h_1, m_1)