import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 현재 나의 depth와, 나의 sub tree 중 가장 깊은 depth의 차를 구함
def measure_depth(start, curDepth):
    depth[start] = curDepth
    maxD = curDepth
    visited[start] = True
    for nxt in graph[start]:
        if not visited[nxt]:
            maxD = max(maxD, measure_depth(nxt, curDepth + 1))
    
    maxDepth[start] = maxD - curDepth
    return maxD


def dfs(start):
    res = 0
    visited[start] = True
    for nxt in graph[start]:
        # maxDepth가 d 미만, 즉 start의 sub tree의 모든 리프 노드까지의 거리가 힘(d) 이내라면 더 깊게 가지 않는다
        if maxDepth[nxt] >= d and not visited[nxt]:
            # 각 자식마다 왔다 갔다 해야하므로 +2
            res += dfs(nxt) + 2
    return res


n, s, d = map(int, input().split())
graph = [[] for _ in range(n+1)]
depth = [0] * (n+1)
maxDepth = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
measure_depth(s, 0)

visited = [False] * (n+1)
print(dfs(s))