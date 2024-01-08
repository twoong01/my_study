def solution(players, callings):
    dic = {f: i for i, f in enumerate(players)}
    for name in callings:
        now_rank = dic[name]
        
        dic[name] -= 1
        dic[players[now_rank - 1]] += 1
        
        players[now_rank - 1], players[now_rank] = name, players[now_rank - 1]
    return players