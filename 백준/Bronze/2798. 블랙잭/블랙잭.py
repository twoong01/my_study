n, m = map(int, input().split())
lst_1 = list(map(int, input().split()))

total_hap = []
for i in range(len(lst_1)):
    for j in range(i+1, len(lst_1)):
        for k in range(j+1, len(lst_1)):
            hap = 0
            hap += lst_1[i] + lst_1[j] + lst_1[k]
            if hap <= m:
                total_hap.append(hap)

print(max(total_hap))