from itertools import combinations
from collections import defaultdict, deque

def solution(relation):
    answer = 0
    data = defaultdict(set)
    
    for row in relation:
        for attrCnt in range(1, len(row)+1):
            for comb in combinations(range(len(row)), r=attrCnt):
                hash = ''.join(map(str, comb))
                val = ''.join(row[i] for i in comb)
                data[hash].add(val)
    
    cand = (key for key in data if len(data.get(key)) == len(relation))  # 유일성을 만족하는 키들의 제네레이터
    
    # 유일성을 만족하는 키에서 최소성을 만족하지 않는 키들을 제거해야 함.
    # ex) ['0', '01', '02', '03', '12', '012', '013', '023', '123', '0123']
    # 0포함하면, 그뒤로 0포함하는거다제외.. 12포함하고.. 그뒤로 12포함하는거 다 제외.. 그런식으로..
    
    q = deque(map(set, cand))
    while (q):
        key = q.popleft()  # 이때 pop()한 키는 후보키임이 보장됨
        # 큐 슬라이싱: 루프 진입 당시 큐에 있던 원소까지만 모두 pop
        for _ in range(len(q)):
            nextKey = q.popleft()
            if not (key.issubset(nextKey)):
                q.append(nextKey)  # 부분집합 관계가 아니라면 유효한 후보키이므로 큐에 다시 넣어줌
        answer += 1
    
    return answer