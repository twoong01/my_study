def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    isvisited = [False] * len(words)
    tmp = []
    def dfs(i, begin, target, words, cnt, before):       
        if check(before, begin) > 1:
            return
        
        if begin == target:
            tmp.append(cnt)
            return

        
        for j in range(len(words)):
            if isvisited[j]: continue
            isvisited[j] = True
            dfs(j, words[j], target, words, cnt + 1, begin)
            isvisited[j] = False
    
    def check(b, a):
        cnt = 0
        for i in range(len(b)):
            if b[i] != a[i]:
                cnt += 1
        return cnt
        
    
    dfs(0, begin, target, words, 0, '')
    answer = min(tmp)
    return answer