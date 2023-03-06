import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
reachable = [[False] * (n+1) for _ in range(n+1)]
arr = [0]
res = []

for i in range(1, n+1):
    reachable[i][i] = True

# arr와 함께 단방향 그래프 만듦
for i in range(1, n+1):
    j = int(input())
    arr.append(j)
    graph[i].append(j)
    
# start에서 시작하여 도달할 수 있는 정점에 reachable을 True로 만들어 줌
# 스택 사용
def dfs(start):
    global reachable
    stack = deque()
    visited = [False] * (n+1)
    stack.append(start)
    
    while stack:
        cur = stack.pop()
        visited[cur] = True
        reachable[start][cur] = True
        
        for nxt in graph[cur]:
            if not visited[nxt]:
                stack.append(nxt)

# 모든 정점에 대해 dfs 수행 -> 모든 정점으로부터 갈 수 있는 모든 정점 탐색
for i in range(1, n+1):
    dfs(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        # arr[5] = 5 같은 경우에는 무조건 도달 가능
        if i == j and arr[i] == i:
            res.append(i)
        
        # i, j가 서로 다르다면 양방향, 즉 reachable[i][j]와 reachable[j][i]가 모두 True여야 함
        if i != j and reachable[i][j] and reachable[j][i]:
            res += [i, j]

# 중복 제거 및 정렬
res = list(set(res))
res.sort()

print(len(res))
print(*res, sep="\n")