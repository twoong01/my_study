from datetime import datetime
def solution(today, terms, privacies):
    answer = []
    
    today_y, today_m, today_d = map(int, today.split('.'))
    
    terms_dict = dict()
    for i in terms:
        kind, limit = i.split(' ')
        terms_dict.setdefault(kind, limit)

    
    privacy_lst = []
    for i in privacies:
        contract_date, contract_kind = i.split(' ')
        contract_y, contract_m, contract_d = contract_date.split('.')
        privacy_lst.append([contract_y, contract_m, contract_d, contract_kind])

    for idx, i in enumerate(privacy_lst):
        month = int(i[1]) + int(terms_dict[i[-1]])
        year = int(i[0])
        day = int(i[2])
        while month > 12:
            month -= 12
            year += 1
        
        day -= 1
        if day == 0:
            month -= 1
            day = 28
        
        if month == 0:
            month = 12
            year -= 1
        if datetime(year, month, day) < datetime(today_y, today_m, today_d):
            answer.append(idx + 1)
        
    return answer