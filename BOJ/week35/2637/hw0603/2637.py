from collections import defaultdict, deque
import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

data = defaultdict(list)
deps = defaultdict(set)  # k 를 만들기 위해 필요한 부품
referenced = defaultdict(set)  # k 가 있어야 만들 수 있는 부품

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().strip().split())
    data[X].append((Y, K))  # X를 만들기 위해 Y가 K개 필요
    deps[X].add(Y)  # X를 만들기 위해 Y가 필요
    referenced[Y].add(X)  # Y가 있어야 X를 만들 수 있음

# 기본 부품과 중간 부품들의 번호 구분
basic = set()
middle = set()
for k, val in data.items():
    for item in val:
        (basic if item[0] not in data.keys() else middle).add(item[0])

q = deque()
for k in deps:
    deps[k] -= basic  # 차집합 연산
    if not (deps[k]):
        q.append(k)  # 기본 부품들만으로 만들 수 있는 중간 부품들(의존성 없는 부품들)을 모두 큐에 삽입

result = {}
while (q):
    partIdx = q.popleft()
    result[partIdx] = defaultdict(int)
    for y, k in data[partIdx]:
        # 중간 부품이라면 그것을 구성하는 부품들의 카운트를 각각 증가
        if (y in middle):
            for a, b in result[y].items():
                result[partIdx][a] += b*k
        # 기본 부품이라면 자신의 카운트를 증가
        else:
            result[partIdx][y] += k
    
    # 나 때문에 의존성 걸렸던 애들 해제
    for p in referenced[partIdx]:
        deps[p] -= {partIdx}  # 차집합 연산
        if not (deps[p]):
            q.append(p)  # 의존성이 모두 해제된 부품은 큐에 추가


for k in sorted(result[N]):
    print(k, result[N][k])
