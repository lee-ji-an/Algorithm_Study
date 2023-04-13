import sys
import heapq
input = sys.stdin.readline

n, m, t = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
conquered = []
heap = []
ans = 0

for _ in range(m):
    node1, node2, cost = map(int, input().split())
    graph[node1].append((cost, node1, node2))
    graph[node2].append((cost, node2, node1))

def include(p):
    global ans
    visited[p] = True
    conquered.append(p)
    for nxt in graph[p]:
        heapq.heappush(heap, nxt)

include(1)

while heap and len(conquered) < n:
    cur = heapq.heappop(heap)
    if visited[cur[1]] and visited[cur[2]]: continue

    ans += cur[0] + (len(conquered)-1) * t

    if not visited[cur[1]]:
        include(cur[1])
    else:
        include(cur[2])

print(ans)