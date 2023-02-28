n = int(input())
S = []
for i in range(n):
    word = str(input())
    word_len = len(word)
    S.append((word, word_len))
# 중복 삭제
S = list(set(S))
# 단어 숫자 -> 단어 알파벳 정렬
S.sort(key=lambda x:(x[1], x[0]))

for i in S:
    print(i[0])
