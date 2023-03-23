import sys
from collections import deque
input = sys.stdin.readline


def bfs(a, b):
    q = deque()
    dist = [[-1, -1] for _ in range(n+1)]
    dist[a][0] = 0
    dist[b][1] = 0
    
    q.append((a, 0, 0))
    q.append((b, 0, 1))
    
    while q:
        node, d, isa = q.popleft()
        
        for nxt in graph[node]:
            # 방문하지 않은 점에 대해서 (거리 -1)
            if dist[nxt][isa] == -1:
                dist[nxt][isa] = d + 1
                # 이전에 반대쪽 노드에서 방문을 한 적이 있다면, LCA 찾았음
                # isa-1 하면 isa가 0일 때 [-1] 이므로 1, 1일 때 0, 즉 반대편을 가리킨다
                if dist[nxt][isa - 1] != -1:
                    return nxt
                q.append((nxt, d+1, isa))
    

for _ in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[b].append(a)
    
    a, b = map(int, input().split())
    print(bfs(a, b))