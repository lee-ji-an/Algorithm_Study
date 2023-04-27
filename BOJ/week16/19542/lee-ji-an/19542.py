import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, S, D = map(int, input().split())

adj = {i: [] for i in range(1, N+1)}
q = deque()

for i in range(N-1):
    v, w = map(int, input().split())
    adj[v].append(w)
    adj[w].append(v)


def get_parent_and_depth():
    parent_list = [-1] * (N+1)
    depth_list = [-1] * (N+1)
    q = deque()
    q.append((S, 0))
    parent_list[S] = 0
    depth_list[S] = 0
    while q:
        node, depth = q.popleft()
        for v in adj[node]:
            if parent_list[v] >= 0:
                continue
            parent_list[v] = node
            depth_list[v] = depth+1
            q.append((v, depth+1))
    return parent_list, depth_list


def get_dist():
    leaf = []
    dist_list = [-1] * (N+1)
    for i in range(1, N+1):
        if len(adj[i]) == 1 and i != S:
            leaf.append(i)
    leaf.sort(key=lambda x: depth_list[x], reverse=True)

    for node in leaf:
        v = node
        dist = 0
        while True:
            dist_list[v] = dist
            if v == S:
                break
            dist += 1
            v = parent_list[v]
            if dist_list[v] >= 0:
                break
    return dist_list


def dfs(vertex):
    global ans
    for w in adj[vertex]:
        if not visited[w] and dist_list[w] >= D:
            visited[w] = True
            ans += 1
            dfs(w)
            visited[w] = False
            ans += 1


# bfs 탐색으로 부모 노드와 depth 를 구함
parent_list, depth_list = get_parent_and_depth()
# leaf node 로부터의 거리를 구함
dist_list = get_dist()

# dfs 탐색으로 이동해야 하는 거리 구하기
visited = [False] * (N+1)
ans = 0
visited[S] = True
dfs(S)
print(ans)

