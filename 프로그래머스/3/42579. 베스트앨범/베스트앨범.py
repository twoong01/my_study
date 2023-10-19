def solution(genres, plays):
    answer = []
    tmp = dict()
    for idx, value in enumerate(genres):
        if value not in tmp:
            tmp.setdefault(value, [[idx, plays[idx]]])
        else:
            tmp[value].append([idx, plays[idx]])
    for key, value in tmp.items():
        tmp_value = sorted(value, key = lambda x : x[1], reverse=True)
        tmp[key] = tmp_value
    
    total_play = {}
    for key, value in tmp.items():
        key_play = sum(play for _, play in value)
        total_play[key] = key_play
    
    # 장르별 재생 횟수 합산을 기준으로 내림차순 정렬
    total_play = dict(sorted(total_play.items(), key=lambda x: x[1], reverse=True))
    
    for key in total_play.keys():
        songs = tmp[key]
        songs = sorted(songs, key=lambda x: (-x[1], x[0]))

        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])
            
    return answer