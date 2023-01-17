from collections import deque
import sys

N = int(sys.stdin.readline())
graph = {i: set() for i in range(N+1)}
visited = [False] * (N+1)
for _ in range(N-1):
    n, v = map(int, sys.stdin.readline().split())
    graph[n].add(v)
    graph[v].add(n)
q = deque(list(map(int, sys.stdin.readline().split())))

def dfs(node: int=1):
    global count

    if (visited[node]):
        return
    visited[node] = True

    # 여기서 q[0]이 현재 노드와 인접하다면 그 노드를 먼저 방문하게 해야 함
    for _ in range(len(graph[node])): # 일단 인접한 노드 개수만큼 방문 시도하는건 자명
        if not (q):
            break
        nextPath = q[0]  # 다음 경로라고 주어진 노드

        if (nextPath in graph[node]):  # 실제로 갈 수 있는 노드(=인접 노드)이고
            if not (visited[nextPath]):  # 아직 방문하지 않았다면
                q.popleft()  # 방문할 것이므로 큐에서 pop하고
                dfs(nextPath)  # 재귀호출하여 방문

if (q.popleft() == 1):
    dfs()  # 경로의 시작이 1번 노드일 때만 진행
else:
    q = True
print(0 if q else 1)  # 탐색 끝난 후 큐가 비어있지 않으면 경로가 잘못된 것!
