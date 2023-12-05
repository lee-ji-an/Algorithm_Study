from itertools import combinations


def solution(relation):  
    columnNum = len(relation[0])
    rowNum = len(relation)
    candidate = set()
    
    for i in range(1, columnNum + 1):
        for idxs in combinations(range(columnNum), i):      # 모든 인덱스 조합을 뽑아봄
            
            temp = set([tuple([row[idx] for idx in idxs]) for row in relation])
            # 해당 인덱스 조합으로 set을 만들어서, 중복을 체크함.
            
            if len(temp) != rowNum:     # 중복이 있다면 패스
                continue
            for c in candidate:     # 중복이 없다면, 기존에 저장된 인덱스를 뽑아서 부분 집합이 되는지 확인함.
                if set(c).issubset(idxs):
                    break
            else:
                candidate.add(idxs)
                
    return len(candidate)