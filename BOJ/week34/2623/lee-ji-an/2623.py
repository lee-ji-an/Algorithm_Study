import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = []
ans = []
in_degree = [0] * (N + 1)
adj = [set() for _ in range(N + 1)]
visited = [[False] * (N + 1) for _ in range(N + 1)]
q = deque()

for m in range(M):
    sequence.append(list(map(int, input().split())))

# Topological Sort를 위한 노드, 간선 설정
for m in range(M):
    for j in range(1, len(sequence[m]) - 1):
        start, end = sequence[m][j], sequence[m][j + 1]
        if visited[start][end]:  # 입력 중 같은 순서가 있을 수 있으므로 visited 체크
            continue
        visited[start][end] = True
        in_degree[end] += 1
        adj[start].add(end)

# Topological Sort
for n in range(1, N + 1):
    if in_degree[n] == 0:
        q.append(n)

while q:
    start = q.popleft()
    ans.append(start)
    for end in adj[start]:
        in_degree[end] -= 1
        if in_degree[end] == 0:
            q.append(end)

if len(ans) == N:
    for a in ans:
        print(a)
else:
    print(0)
