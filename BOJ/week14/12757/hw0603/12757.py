import bisect
import sys

N, M, K = map(int, sys.stdin.readline().split())
JBNU = {}
sortedkeys = []


# insort로 키 리스트에 키를 삽입하여 정렬된 상태 유지
def addSortedKey(key):
    bisect.insort(sortedkeys, key)

# DB에 값 추가
def add(key, value):
    JBNU[key] = value
    addSortedKey(key)

# DB에 K 범위 안의 Key가 있는지 검색
def search(key):
    # 원본 key에 해당하는 value가 존재한다면 바로 반환
    if (JBNU.get(key, None)):
        return key
    
    keyIdx = bisect.bisect_left(sortedkeys, key)
    # key의 bisect 결과가 첫 번째 인덱스일 때
    if (keyIdx == 0):
        if (abs(sortedkeys[0]-key) <= K):
            return sortedkeys[0]
    # key의 bisect 결과가 마지막 인덱스일 때
    elif (keyIdx == len(sortedkeys)):
        if (abs(sortedkeys[keyIdx-1]-key) <= K):
            return sortedkeys[keyIdx-1]
    else:
        l_cand, r_cand = sortedkeys[keyIdx-1], sortedkeys[keyIdx]
        # 조건을 만족하는 Key가 2개 존재
        if (r_cand-key == key-l_cand):
            return -2
        # l_cand가 조건을 만족
        if (key-l_cand < r_cand-key):
            if (key-l_cand <= K):
                return l_cand
        # r_cand가 조건을 만족
        if (r_cand-key < key-l_cand):
            if (r_cand-key <= K):
                return r_cand

    # 조건을 만족하는 Key가 없음
    return -1

# DB에서 Key에 해당하는 값 수정
def change(key, value):
    # key로 검색된 결과가 유일하지 않으면 무시함
    if ((tmpkey := search(key)) not in {-1, -2}):
        JBNU[tmpkey] = value

# Key에 해당하는 값 출력
def show(key):
    # 조건을 만족하는 key가 없는 경우 -1 출력
    # 값이 두 개 이상 존재하는 경우 '?' 출력
    print(-1 if (tmpkey := search(key)) == -1 else "?" if tmpkey == -2 else JBNU[tmpkey])



# 초기 데이터 구축
for _ in range(N):
    k, v = map(int, sys.stdin.readline().split())
    add(k, v)

# 쿼리문 실행
for _ in range(M):
    op, *kv = map(int, sys.stdin.readline().split())

    match (op):
        case 1:
            add(*kv)
        case 2:
            change(*kv)
        case 3:
            show(kv[0])
