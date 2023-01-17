import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [set() for _ in range(n+1)]
# 그래프의 간선을 set 형태로 저장
for _ in range(n-1):
    p, q = map(int, input().split())
    graph[p].add(q)
    graph[q].add(p)

seq = deque(list(map(int, input().split())))

def bfs(start):
    q = deque()
    visited = [False] * (n+1)
    q.append(start)
    visited[start] = True
    while q:
        cur = q.popleft()
        for _ in range(len(graph[cur])):
            # seq[0]이 있으면 성공적으로 뺄 수 있다. 뺀 후에는 BFS를 위해 탐색 큐 뒤에 붙인다.
            if seq[0] in graph[cur] and not visited[seq[0]]:
                visited[seq[0]] = True
                q.append(seq.popleft())
                # seq가 비었으면 모두 탐색 성공한 것이므로 성공
                if not seq:
                    print(1)
                    exit()
    return False

if seq[0] != 1:
    print(0)
    exit()

if not bfs(seq.popleft()):
    print(0)