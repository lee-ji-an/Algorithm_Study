import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
topo = []
q = deque()

for _ in range(m):
    t = list(map(int, input().split()))
    for i in range(1, t[0]):
        graph[t[i]].append(t[i+1])
        indegree[t[i+1]] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    c = q.popleft()
    topo.append(c)

    for nxt in graph[c]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

if len(topo) == n:
    print(*topo, sep="\n")
else:
    print(0)