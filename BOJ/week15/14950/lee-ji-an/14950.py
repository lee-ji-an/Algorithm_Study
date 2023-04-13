import heapq
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
adj = {k: [] for k in range(1, N + 1)}
heap = []
complete_city = set()
cost = 0
plus_cost = 0

for i in range(M):
    v, w, weight = map(int, input().split())
    adj[v].append((w, weight))
    adj[w].append((v, weight))

for w, weight in adj[1]:
    heapq.heappush(heap, (weight, w))
complete_city.add(1)

while heap:
    # 정복할 도시 pop
    weight, w = heapq.heappop(heap)
    if w in complete_city:
        continue
    complete_city.add(w)
    cost += weight + plus_cost
    plus_cost += T
    # 새롭게 갈 수 있는 경로를 추가
    for adj_city, adj_weight in adj[w]:
        if adj_city in complete_city:  # 이미 정복한 도시는 제외
            continue
        heapq.heappush(heap, (adj_weight, adj_city))

print(cost)
