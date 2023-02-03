bingo, mc = [], []
ans_sheet = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    bingo.append(list(map(int, input().split())))
for i in range(5):
    mc.append(list(map(int, input().split())))
bingo_count = 0
for i in range(5):
    for j in range(5):
        bingo_count = 0
        for ci in range(5):
            for cj in range(5):
                if mc[i][j] == bingo[ci][cj]:
                    ans_sheet[ci][cj] = 1
                    break

        hap = 0
        # 가로 빙고 확인
        for k in range(5):
            hap = 0
            for l in range(5):
                hap += ans_sheet[k][l]
                if hap == 5:
                    bingo_count += 1

        # 세로 빙고 확인
        for k in range(5):
            hap = 0
            for l in range(5):
                hap += ans_sheet[l][k]
                if hap == 5:
                    bingo_count += 1
        hap = 0
        # 대각석 빙고 확인
        for k in range(5):
            hap += ans_sheet[k][k]
            if hap == 5:
                bingo_count += 1

        hap = 0
        # 대각선 빙고 확인
        for k in range(5):
            hap += ans_sheet[k][4 - k]
            if hap == 5:
                bingo_count += 1


        # 전체 빙고 갯수 확인
        if bingo_count >= 3:
            print(i * 5 + j + 1)
            exit()