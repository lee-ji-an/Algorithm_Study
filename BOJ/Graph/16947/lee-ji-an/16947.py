import sys
from collections import deque
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

N = int(input())
adj = [[] for i in range(N)]
stack = [-1 for i in range(N)]
visited = [0 for i in range(N)]

cycle = [-1 for i in range(N)]
popList = []
top = -1
distance = [0 for i in range(N)]
# dfs를 하다가 이미 방문한 지점을 만나면 해당 지점이 나올 때까지 stack을 pop해서 나오는 것들이 곧 사이클에 포함되는 node
flag = True
def dfs(v, parent):
    if visited[v]:
        return
    visited[v] = True
    for w in adj[v]:
        if w == parent:   # 부모 노드로 다시 돌아가는 것 방지
            continue
        if not visited[w]:
            res = dfs(w, v)
            if res >= 0:       # cycle 찾았을 때
                cycle[v] = 0
                if res != v:   # cycle을 찾았지만 cycle의 시작점을 아직 찾는 중일 경우
                    return res
                else:
                    return -2    # cycle의 시작점을 찾았을 때
            elif res == -2:
                return -2
        else:                   # 이미 방문한 노드를 다시 방문한 경우 -> cycle 발견
            cycle[v] = 0        # 그 노드의  w (부모 노드) 가 cycle의 시작이므로 그 값을 return해 줌
            return w
    return -1


def bfs():             # multisource BFS (순환선의 모든 역을 bfs의 출발점으로 설정)
    q = deque()
    for i in range(N):
        if cycle[i] == 0:
            q.append((i, 0))
            visited2[i] = 1
    while q:
        vertex, dist = q.pop()
        for w in adj[vertex]:
            if not visited2[w]:
                cycle[w] = dist+1
                visited2[w] = 1
                q.append((w, dist+1))



for i in range(N):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    adj[a].append(b)
    adj[b].append(a)

dfs(0, -1)
visited2 = [0 for j in range(N)]
bfs()
for i in range(len(cycle)):
    print(cycle[i], end=" ")