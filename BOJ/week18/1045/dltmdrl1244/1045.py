import sys
import heapq
input = sys.stdin.readline

########## Union Find 관련 함수 ##########
def root(p):
    while ids[p] != p:
        p = ids[p]
    return p

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    if connected(p, q):
        return
    
    a, b = root(p), root(q)
    if size[a] >= size[b]:
        size[a] += size[b]
        ids[b] = a
    else:
        size[b] += size[a]
        ids[a] = b
    
########## Union Find 관련 함수 ##########

n, m = map(int, input().split())
edges = []
answer = [0] * n
ids = [i for i in range(n)]
size = [1 for _ in range(n)]
edge_count = 0

for i in range(n):
    t = list(input().rstrip())
    for j in range(i, n):
        if t[j] == 'Y':
            edge_count += 1
            heapq.heappush(edges, (i, j))

# 총 edge 개수보다 m이 크면 답 X
if edge_count < m:
    print(-1)
    exit()

count = 0
not_selected = [] # MST를 구성하고 남은 edges
while edges:
    t = heapq.heappop(edges)
    # 서로 연결되지 않은 노드들이라면 연결함
    if not connected(t[0], t[1]):
        union(t[0], t[1])

        answer[t[0]] += 1
        answer[t[1]] += 1
        count += 1
        if count == n - 1:
            # 나머지 노드들을 not_selected에 옮겨 담음
            while edges:
                heapq.heappush(not_selected, heapq.heappop(edges))

    # 연결된 노드들도 일단 not_selected에 저장
    else:
        heapq.heappush(not_selected, t)

# m개가 될 때까지 우선 순위가 가장 높은 튜플들을 꺼내어 기록함
while count != m:
    t = heapq.heappop(not_selected)
    answer[t[0]] += 1
    answer[t[1]] += 1
    count += 1

# connected component가 몇 개인지 확인
idset = set()
for i in range(n):
    idset.add(root(i))
    
if len(idset) == 1:
    print(*answer)
else:
    print(-1)