def solution(record):
    answer = []
    idToName = {}       # 아이디와 이름을 매칭하는 딕셔너리
    
    record = [r.split() for r in record]
    for r in record:
        if r[0] != 'Leave':
            idToName[r[1]] = r[2]       # 최종 이름과 매칭함.
    
    for r in record:
        if r[0] == 'Enter':
            answer.append(f'{idToName[r[1]]}님이 들어왔습니다.')
        elif r[0] ==  'Leave':
            answer.append(f'{idToName[r[1]]}님이 나갔습니다.')

    return answer