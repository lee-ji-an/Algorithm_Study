from collections import defaultdict, deque
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

data = defaultdict(list)
refCnt = defaultdict(set)
deps = defaultdict(set)

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().strip().split())
    data[X].append((Y, K))
    refCnt[X].add(Y)
    deps[Y].add(X)

# 기본 부품과 중간 부품 구분
basic = set()
middle = set()
for k, val in data.items():
    for item in val:
        (basic if item[0] not in data.keys() else middle).add(item[0])

# print(basic, middle)

result = {}
q = deque()
for k in refCnt:
    refCnt[k] -= basic  # 차집합 연산
    if (len(refCnt[k]) == 0):
        q.append(k)  # 기본 부품들만으로 만들 수 있는 중간 부품들을 다 큐에 삽입

for p in basic:
    del deps[p]

while (q):
    partIdx = q.popleft()
    result[partIdx] = {}
    for y, k in data[partIdx]:
        if (y in middle):
            for a, b in result[y].items():
                if (result[partIdx].get(a)):
                    result[partIdx][a] += b*k
                else:
                    result[partIdx][a] = b*k
        else:
            if (result[partIdx].get(y)):
                result[partIdx][y] += k
            else:
                result[partIdx][y] = k
    
    # 나 때문에 의존성 걸렸던 애들 해제
    for p in deps[partIdx]:
        refCnt[p] -= {partIdx}
        if (len(refCnt[p]) == 0):
            q.append(p)


# print(refCnt)
# print(data)
# print(deps)
# print(result)

for k in sorted(result[N]):
    print(k, result[N][k])