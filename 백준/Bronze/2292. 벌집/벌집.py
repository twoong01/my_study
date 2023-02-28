finish = int(input())

way = 1
for n in range(finish+1):
    way += n*6

    if finish == 1:
        break
    if finish <= way:
        break
print(n+1)