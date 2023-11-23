from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    db = defaultdict(list)

    # 데이터 삽입
    for *key, score in map(str.split, info):
        for itemCnt in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for hash in combinations(key, itemCnt):
                db[''.join(hash)].append(int(score))

    # 이진탐색을 활용하기 위해 각 해시들의 리스트 정렬
    for k in db:
        db[k].sort()
    
    # 데이터 검색
    for *queryKey, score in map(lambda x: x.replace("and", '').split(), query):
        queryKey = ''.join(queryKey).replace('-', '')  # 해시 생성
        scores = db.get(queryKey, [])
        answer.append(len(scores) - bisect_left(scores, int(score)))

    return answer
