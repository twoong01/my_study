import sys
import collections
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
print(round(sum(num)/n))
print(num[(n//2)])
def freq(num):
    tmp = collections.Counter(num).most_common()
    if len(tmp) > 1:
        if tmp[0][1] == tmp[1][1]:
            return tmp[1][0]
        else:
            return tmp[0][0]
    else:
        return tmp[0][0]
print(freq(num))
print(max(num) - min(num))
