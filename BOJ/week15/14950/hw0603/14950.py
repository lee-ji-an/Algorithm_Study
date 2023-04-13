import heapq
import sys

N, M, t = map(int, sys.stdin.readline().split())

# 인접리스트 구축
adjList = [[] for _ in range(N+1)]
for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    adjList[A].append((C, B))  # 가중치 먼저
    adjList[B].append((C, A))

visited = [False]*(N+1)
heap = [(0, 1)]  # 1번 도시는 이미 정복한 상태
totalCost = 0  # 총 비용
count = 0  # 추가 정복한 도시 수


# 간선을 모두 연결할 때 까지 Prim
while (heap and count < N):
    cost, node = heapq.heappop(heap)  # 비용, 도시번호
    if (visited[node]):
        continue  # 이미 정복한 도시 Skip

    visited[node] = True
    totalCost += cost
    count += 1

    # 인접한 도시들을 순회하며 힙에 삽입
    for cost, adjCity in adjList[node]:
        heapq.heappush(heap, (cost, adjCity))  # 비용, 도시번호

# 정복하면서 증가했던 비용들 누적해 줌
print(totalCost + t*(N-1)*(N-2)//2)
