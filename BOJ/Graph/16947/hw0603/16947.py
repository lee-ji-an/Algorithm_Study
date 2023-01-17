from collections import deque
import sys
sys.setrecursionlimit(10**8)

NOT_VISITED, VISITED, IN_CYCLE = 0, 1, 2
N = int(sys.stdin.readline())
adjList = {i: list() for i in range(N+1)}  # 인접 리스트로 사용할 딕셔너리
status = [NOT_VISITED] * (N+1)
dist = [NOT_VISITED] * (N+1)  # 각 노드와 순환선 사이의 거리

# 양방향 인접 리스트 구축
for _ in range(N):
    u, v = map(int, sys.stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)

# DFS로 사이클 탐색하고 감지한 사이클의 첫 노드를 반환
def dfs(node=1, cnt=0):
    # 현재 노드가 이미 방문한 노드 and 거리차가 3이상이면 사이클 탐지
    if (status[node] in (VISITED, IN_CYCLE)):  # VISITED or IN_CYCLE
        return node if cnt - dist[node] >= 3 else -1
    
    status[node] = VISITED  # 노드 방문처리
    dist[node] = cnt  # dist에 각 노드에 이르기까지 몇 번 이동했는지 저장
    
    # 현재노드와 인접한 노드에 대해 재귀호출
    for nextNode in adjList[node]:
        # dfs 결과: 처음 사이클을 감지한 노드를 계속해서 반환
        first_node_in_cycle = dfs(nextNode, cnt+1)
        if (first_node_in_cycle != -1):
            status[node] = IN_CYCLE  # DFS 반환 시 마다 스택에 쌓인 노드들(경로 역순)의 상태를 IN_CYCLE로 마킹
            return -1 if node == first_node_in_cycle else first_node_in_cycle
    return -1


dfs()  # 첫 번째 노드부터 사이클 탐색 진행

# BFS를 통해 사이클까지의 거리 계산
q = deque()
for i in range(1, N+1):
    # 사이클 내의 노드들을 모두 큐에 넣고 거리를 0으로 설정
    if (status[i] == IN_CYCLE):
        q.append(i)
        dist[i] = 0
    else:
        dist[i] = -1  # 사이클에 포함되지 않은 노드는 -1로 마킹
while (q):
    node = q.popleft()
    for nextNode in adjList[node]:
        if (dist[nextNode] == -1):  # nextNode가 사이클 내의 노드가 아닐 때만
            q.append(nextNode)  # 큐에 해당 노드 추가
            dist[nextNode] = dist[node] + 1  # 지선이 시작되는 역: (0) + 1, 다음 역: ((0)+1) + 1 ...

print(' '.join(map(str, dist[1:])))
