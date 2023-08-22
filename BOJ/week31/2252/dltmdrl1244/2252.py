import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
'''
indegree : 필수적으로 내 앞에 와야하는 사람의 남은 수
graph : 내가 필수적으로 어떤 사람들의 앞에 와야 하는지
'''
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
topo = []
visited = [False for _ in range(n+1)]
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

# 선행되어야 하는 사람이 없어서 바로 설 수 있는 사람들은 바로 큐에 넣음
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    # cur은 그 자리에 바로 서면 된다. Topo에 넣고 방문처리
    cur = q.popleft()
    topo.append(cur)
    visited[cur] = True
    
    # Cur을 선행조건으로서 갖는 사람들의 indegree를 감소시키고, Indegree가 0이 되어 설 수 있게 되면 큐에 넣는다
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0 and not visited[nxt]:
            q.append(nxt)

# 선 순서대로 저장되어 있는 리스트
print(*topo)