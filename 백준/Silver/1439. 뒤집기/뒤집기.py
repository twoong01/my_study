import sys
input = sys.stdin.readline

s = input()
cntzero = cntOne = 0
numOne = s.split('0')
numzero = s.split('1')
for i in numOne:
    if i != "" and i != '\n':
        cntOne += 1
for i in numzero:
    if i != "" and i != '\n':
        cntzero += 1
print(min(cntzero, cntOne))