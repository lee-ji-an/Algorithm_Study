import heapq
import sys

N = int(sys.stdin.readline())

string = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
graph = [[] for _ in range(N+1)]
total = 0

for i in range(N):
    for j in range(N):
        if (string[i][j].isnumeric()):
            continue

        k, d = (1, 97) if string[i][j].islower() else (27, 65)  # 대소문자 구분
        weight = ord(string[i][j]) - d + k
        graph[i].append((weight, j))  # heapq 사용할 것이므로 가중치를 먼저 삽입
        graph[j].append((weight, i))
    
        total += weight


# Prim MST
heap = [(0, 0)]
visited = [False] * N

while (heap):
    value, node = heapq.heappop(heap)

    if not (visited[node]):
        visited[node] = True
        total -= value

        for v, n in graph[node]:
            heapq.heappush(heap, (v, n))

# 모든 컴퓨터가 연결되어 있지 않으면 -1 출력
if (any (not v for v in visited)):
    sys.exit(print(-1))

print(total)
