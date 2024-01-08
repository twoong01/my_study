def solution(friends, gifts):
    answer = 0
    dic = {f:i for i, f in enumerate(friends)}
    gift_table = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    presents = [0] * len(friends)
    
    # 선물 주고 받은 테이블
    for gift in gifts:
        give, take = gift.split()
        gift_table[dic[give]][dic[take]] += 1

    # 선물 지수
    gift_rate = []
    for i in range(len(friends)):
        row = sum(gift_table[i])
        col = 0
        for j in range(len(friends)):
            col += gift_table[j][i]
        gift_rate.append(row - col)
    
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if gift_table[i][j] > gift_table[j][i]:
                presents[i] += 1
            elif gift_table[i][j] < gift_table[j][i]:
                presents[j] += 1
            else:
                if gift_rate[i] > gift_rate[j]:
                    presents[i] += 1
                elif gift_rate[i] < gift_rate[j]:
                    presents[j] += 1
    answer = max(presents)
    return answer