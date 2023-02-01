# 별, 동그라미, 네모, 세모를 각각 숫자 4, 3, 2, 1
'''
만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
'''

n = int(input())
for i in range(n):
    A_card = list(map(int, input().split()))
    B_card = list(map(int, input().split()))
    del A_card[0]
    del B_card[0]
    if len(A_card) > len(B_card):
        for _ in range(len(A_card) - len(B_card)):
            B_card.append(0)
    elif len(A_card) < len(B_card):
        for _ in range(len(A_card) - len(B_card)):
            A_card.append(0)
    A_card = sorted(A_card, reverse=True)
    B_card = sorted(B_card, reverse=True)
    for j in range(max(len(A_card), len(B_card))):
        if A_card[j] > B_card[j]:
            print('A')
            break
        elif A_card[j] < B_card[j]:
            print('B')
            break
    else:
        print('D')