def solution(sequence, k):
    answer = []
    summ = 0
    last_index = len(sequence)-1
    for i, v in enumerate(sequence[::-1]):
        summ += v
        # print(i,v)
        if summ < k:
            pass
        elif summ > k:
            summ -= sequence[last_index]
            last_index -= 1
            if summ == k:
                answer.append([len(sequence)-1-i, last_index])

        else: # summ == k
            # print(i)
            answer.append([len(sequence)-1-i, last_index])

    # print(answer)
    answer.sort(key=lambda x : (x[1]-x[0], x[0]))
    # print(answer)
    return answer[0]