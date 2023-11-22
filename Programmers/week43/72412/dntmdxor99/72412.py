import bisect

def solution(info, query):
    answer = []
    table = dict()
    
    for i in ['cpp', 'java', 'python', '-']:
        for j in ['backend', 'frontend', '-']:
            for k in ['junior', 'senior', '-']:
                for s in ['chicken', 'pizza', '-']:
                    table[i + j + k + s] = []       # 다 때려박음..
    
    for data in info:
        data = data.split()
        value = int(data[-1])
        for i in [data[0], '-']:
            for j in [data[1], '-']:
                for k in [data[2], '-']:
                    for s in [data[3], '-']:
                        bisect.insort(table[i + j + k + s], value)
                        # 모든 값들과 후보가 되는 값들을 미리 집어넣음.
    
    for data in query:
        data = data.split(' ')
        key = data[0] + data[2] + data[4] + data[6]
        value = int(data[-1])
        candidate = table[key]
        answer.append(len(candidate) - bisect.bisect_left(candidate, value))
        # 위에서 후보가 되는 값들의 점수를 모두 정렬해서 넣었으므로, 그대로 찾기만 하면 됨
        
    return answer