import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())  # 입력 받기
    adj = [0] * (N + 1)
    for _ in range(N - 1):
        p, c = map(int, input().split())
        adj[c] = p  # 부모 노드만 저장
    start, end = map(int, input().split())

    visited = [False] * (N + 1)
    ans = 0
    q = deque([start, end])
    while q:
        node = q.popleft()
        if visited[node]:
            ans = node
            break

        visited[node] = True
        if adj[node] != 0:  # node 가 루트 노드가 아닐 때 q에 append
            q.append(adj[node])

    print(ans)
