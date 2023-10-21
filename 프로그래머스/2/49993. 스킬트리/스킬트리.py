def solution(skill, skill_trees):
    answer = 0
    skill_list = []
    for i in range(len(skill)):
        skill_list.append(skill[0:i + 1])
    for i in skill_trees:
        tmp = ''
        for j in i:
            if j in skill:
                tmp += j
        if tmp in skill_list:
            answer += 1
        if tmp == '':
            answer += 1
    return answer