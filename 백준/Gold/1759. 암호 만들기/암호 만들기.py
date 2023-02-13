l, c = map(int, input().split())
n_lst = list(map(str, input().split()))
n_lst = sorted(n_lst)
alpha = ['a', 'e', 'i', 'o', 'u']

def back(chosen, cnt_a, cnt_b, idx):
    if len(chosen) == l:
        if cnt_a >= 1 and cnt_b >= 2:
            for ch in chosen:
                print(ch, end='')
            print()
            return
    else:
        for i in range(idx, c):
            chosen.append(n_lst[i])
            if n_lst[i] in alpha:
                back(chosen, cnt_a + 1, cnt_b, i + 1)
            else:
                back(chosen, cnt_a, cnt_b + 1, i + 1)
            chosen.pop()

back([], 0, 0, 0)
