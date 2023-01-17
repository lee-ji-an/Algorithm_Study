import sys
from collections import deque
input = sys.stdin.readline

def dfs(k):
    # 큐가 비었다면 모두 정상적으로 pop 된 것이므로 성공
    if not q:
        print(1)
        exit()

    visited[k] = True
    # 한 정점 k에서부터 뻗어나가는 간선 개수만큼 반복
    for _ in range(len(graph[k])):
        # 다음에 탐색되어야 할 노드가 k와 인접한 노드들 중에 있는지, 있다면 DFS이므로 그 노드에서 한번 더 DFS 수행
        if q[0] in graph[k] and not visited[q[0]]:
            dfs(q.popleft())

    return False

n = int(input())
# 그래프 간선을 리스트가 아닌 set으로 저장 (연결 가능한지 여부만 판단할 것이므로)
graph = [set() for _ in range(n+1)]

visited = [False] * (n+1)

for _ in range(n-1):
    i, j = map(int, input().split())
    graph[i].add(j)
    graph[j].add(i)

seq = list(map(int, input().split()))
q = deque(seq)

if seq[0] != 1:
    print(0)
    exit()

# 리스트 맨 앞의 원소(탐색 시작점 = 1)를 삭제함과 동시에 파라미터로 넘긴다
if not dfs(q.popleft()):
    print(0)