t = int(input())
for i in range(t):
    l = list(str(input()))
    score = []
    for i in range(len(l)):
        if l[i] == 'X':
            score.append(0)
        else:
            if i == 0:
                score.append(1)
            else:
                score.append(score[i-1] + 1)
    print(sum(score))
