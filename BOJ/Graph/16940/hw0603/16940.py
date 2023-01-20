from collections import deque
import sys

N = int(sys.stdin.readline())
graph = {k: set() for k in range(1, N+1)}
visited = [False] * (N+1)

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].add(v)
    graph[v].add(u)

user_path = deque(map(int, sys.stdin.readline().split()))
if (user_path.popleft() != 1):  # 문제 조건에 의해 시작 정점이 1이 아닌 경우 잘못된 경로
    print(0)
    sys.exit()

# 1번 노드를 시작 지점으로 BFS
q = deque((1,))
visited[1] = True
result = -1
while (q):
    x = q.popleft()
    # 노드 x의 인접 노드 중 방문하지 않은 것들의 집합을 구하고,
    # 구한 집합의 원소 개수만큼 user_path의 앞에서부터 집합을 만들었을 때,
    # 두 집합이 같아야 함
    
    # 노드 x의 인접 노드 중 방문하지 않은 집합
    adjNotVisited = {node for node in graph[x] if not visited[node]}
    # adjNotvisited와 길이만큼 user_path에서 뽑아온 집합
    will = {user_path[i] for i in range(len(adjNotVisited))}

    # 두 집합이 다르면 경로가 잘못된 것
    if (adjNotVisited != will):
        result = 0
        break

    # 실제 BFS로 동작할 수 있게 큐에 추가해 줌
    # 단, user_path 순서에 맞게 추가
    for _ in range(len(adjNotVisited)):
        nextnode = user_path.popleft()
        visited[nextnode] = True
        q.append(nextnode)
    

print(1 if result else 0)
