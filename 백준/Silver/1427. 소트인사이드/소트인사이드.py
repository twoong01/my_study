array = list(map(int, input()))
array.sort(reverse=True)
for i in range(len(array)):
    print(array[i], end='')
    