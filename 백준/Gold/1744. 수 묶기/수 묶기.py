import sys
input = sys.stdin.readline

n = int(input())
graph = []
positiveList = []
negativeList = []
oneList = []
for i in range(n):
    num = int(input())
    if num > 1:
        positiveList.append(num)
    elif num <= 0:
        negativeList.append(num)
    else:
        oneList.append(num)
positiveList.sort(reverse=True)
negativeList.sort()

result = 0
if len(positiveList)%2 == 0:
    for i in range(0,len(positiveList),2):
        result += positiveList[i]*positiveList[i+1]
else:
    for i in range(0,len(positiveList)-1,2):
        result += positiveList[i]*positiveList[i+1]
    result += positiveList[len(positiveList)-1]

if len(negativeList)%2 == 0:
    for i in range(0,len(negativeList),2):
        result += negativeList[i]*negativeList[i+1]
else:
    for i in range(0,len(negativeList)-1,2):
        result += negativeList[i]*negativeList[i+1]
    result += negativeList[len(negativeList)-1]

result += sum(oneList)
print(result)

    
