import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
prev = [-1 for _ in range(n)]
cycles = []
dist = [-1 for _ in range(n)]

# 사이클의 양 끝점을 이용해 prev 값을 추적하면서 사이클을 구성하는 원소들을 리턴
def find_cycle(start, end):
    mylist = [start, end]
    while prev[start] != end:
        mylist.append(prev[start])
        start = prev[start]
    return mylist

# 0에서 dfs 수행하여 prev 기록
def dfs(start):
    global prev, cycles
    q = deque()
    q.append((start, start))

    while q:
        cur, p = q.pop()
        # prev가 -1이 아니면 이미 방문했음
        if prev[cur] != -1:
            return
        prev[cur] = p
        for i in graph[cur]:
            if i == p:
                continue

            if prev[i] != -1:
                cycles = [cur, i]
            # 아직 방문하지 않은 점에 대해 append
            else:
                q.append((i, cur))

def bfs(k):
    global dist
    q = deque()
    q.append((k, 0))
    visited = [False for _ in range(n)]
    visited[k] = True
    while q:
        cur, d = q.popleft()
        for i in graph[cur]:
            if i in cycles or visited[i]:
                continue

            if dist[i] == -1:
                dist[i] = d + 1

            q.append((i, d + 1))
            visited[cur] = True

def find_dist(k):
    q = deque()
    q.append((k, 0))
    visited = [False for _ in range(n)]
    visited[k] = True

    while q:
        (cur, dist) = q.popleft()
        visited[cur] = True
        # print("cur : ", cur)
        for i in graph[cur]:
            if i in cycles:
                return dist + 1

            if not visited[i]:
                q.append((i, dist + 1))

for _ in range(n):
    p, q = map(int, input().split())
    p, q = p-1, q-1
    graph[q].append(p)
    graph[p].append(q)

dfs(0)
# cycles에는 초기에 사이클의 양 끝점이 들어 있음
cycles = set(find_cycle(cycles[0], cycles[1]))

# bfs로 사이클 내의 점에서부터 뻗어나가며 최단거리 계산
for i in range(n):
    if i in cycles:
        dist[i] = 0
        bfs(i)

print(*dist)