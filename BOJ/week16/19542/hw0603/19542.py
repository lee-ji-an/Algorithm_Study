import sys
sys.setrecursionlimit(10**9)

N, S, D = map(int, sys.stdin.readline().split())
graph = [list() for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, prevNode):
    global answer

    distFromLeaf = 0
    for nextNode in graph[node]:
        if (nextNode == prevNode):  # 중복방문 방지
            continue
        distFromLeaf = max(dfs(nextNode, node), distFromLeaf)  # DFS 탐색. 제일 깊은 노드까지 고려해야 하므로 최댓값을 기준으로.
    if (distFromLeaf >= D):  # 리프노드에서 현재노드까지의 거리가 D 이상이면 ans 증가
        answer += 1
    return distFromLeaf+1  # 재귀스택 풀리면서 1씩 증가

answer = 0
dfs(S, 0)  # 루트노드: 케니소프트
print(2*(answer-1) if answer else 0)  # 왕복거리이므로 2를 곱해줌
