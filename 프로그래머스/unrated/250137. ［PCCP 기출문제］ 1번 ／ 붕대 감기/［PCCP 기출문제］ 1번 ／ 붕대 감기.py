def solution(bandage, health, attacks):
    max_health = health
    t, x, y = bandage
    attack_idx = 0
    bandage_cnt = 0
    last_attack_time = attacks[-1][0]
    for time in range(1, last_attack_time + 1):
        if time == attacks[attack_idx][0]:
            health -= attacks[attack_idx][1]
            attack_idx += 1
            bandage_cnt= 0
            if health <= 0:
                return -1
        else:
            health += x
            bandage_cnt += 1
            if bandage_cnt == t:
                health += y
                bandage_cnt= 0
            if health > max_health:
                health = max_health
    return health