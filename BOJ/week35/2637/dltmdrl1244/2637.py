import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
q = deque()
counts = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    # x를 만들기 위해 y가 k개 필요하다
    x, y, k = map(int, input().split())
    indegree[x] += 1
    graph[y].append((x, k))


for i in range(1, n+1):
    # 여기서 i는 모두 기본 부품의 번호
    # i를 만들기 위해선 i가 1개 필요함
    if indegree[i] == 0:
        q.append(i)
        counts[i][i] = 1

while q:
    cur = q.popleft()
    # 이제 cur을 만들기 위한 모든 하위 부품을 확인했으므로 cur을 만드는데 필요한 부품의 최종 수는 확정됐음

    for nxtIdx, nxtCount in graph[cur]:
        # cur을 하위 부품으로 가지는 상위 부품을 만드는 데 필요한 개수 counts[nxt]를 counts[cur]에다가 cur 개수를 곱해서 더해나감
        counts[nxtIdx] = [i * nxtCount + j for i, j in zip(counts[cur], counts[nxtIdx])]
        indegree[nxtIdx] -= 1
        if indegree[nxtIdx] == 0:
            q.append(nxtIdx)

for i in range(n+1):
    if counts[-1][i]:
        print(i, counts[-1][i])