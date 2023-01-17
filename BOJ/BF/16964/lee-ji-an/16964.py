import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
check = [False] * N
level = [-1 for _ in range(N)]
ptr = 0
flag = True


def bfs():  # bfs로 root노드에서부터 모든 정점까지의 depth(거리)를 구함
    visited = [0 for _ in range(N)]
    q = deque()
    q.append((checkDfs[0], 0))
    visited[checkDfs[0]] = 1
    while q:
        v, dist = q.pop()
        level[v] = dist
        for w in adj[v]:
            if not visited[w]:
                q.append((w, dist + 1))
                visited[w] = 1


def dfsTester():    # depth가 증가할 때 depth가 깊은 쪽의 노드가 depth가 얕은 쪽 노드의 자식이어야 함
    for i in range(len(checkDfs) - 1):
        if level[checkDfs[i]] < level[checkDfs[i + 1]]:
            if checkDfs[i + 1] in adj[checkDfs[i]]:
                continue
            else:
                return False
    return True

    # global flag, ptr
    # check[node] = True
    # while len(adj[node]) > 0 and flag:
    #     if checkDfs[ptr+1] in adj[node]:
    #         adj[node].remove(checkDfs[ptr+1])
    #         adj[checkDfs[ptr+1]].remove(node)
    #         ptr += 1
    #         dfsTester(checkDfs[ptr])
    #     else:
    #         flag = False
    #         return


adj = [[] for i in range(N)]

for i in range(N - 1):
    v, w = map(int, input().split())
    v, w = v - 1, w - 1
    adj[v].append(w)
    adj[w].append(v)
checkDfs = list(map(int, input().split()))
for i in range(len(checkDfs)):
    checkDfs[i] = checkDfs[i] - 1

if checkDfs[0] == 0:
    bfs()
    print(int(dfsTester()))
else:
    print(0)
