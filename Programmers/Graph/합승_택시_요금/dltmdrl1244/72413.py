import heapq

# 다익스트라 알고리즘
# 각 노드까지의 거리를 heapq (우선순위 큐)에다 저장하여, 매번 가장 짧은 거리를 뽑아낼 수 있다.
def dijkstra(start, graph):
    dist = [float('inf') for _ in range(len(graph))]
    dist[start] = 0
    q = []
    # 시작은 출발점과 출발점으로부터 출발점까지의 거리(0)을 넣어줌
    heapq.heappush(q, (start, 0))

    while q:
        # heapq에 저장된 특정 노드까지의 최단거리들 중 가장 짧은 정보를 빼낸다.
        # 그러면 그 노드로 가는 최단거리는 무조건 지금 빼낸 정보임이 보장된다.
        # 그 노드의 최단거리를 확정한다.
        node, distance = heapq.heappop(q)

        for n in graph[node]:
            new_cost = n[1] + dist[node]
            # 만약 지금 빼낸 노드로부터 이웃한 노드들의 거리를 보았을 때
            # (현재 heapq에 저장된 특정 노드까지의 최단거리) > (지금 빼낸 노드까지의 거리) + (지금 빼낸 노드에서부터 그 노드까지의 거리) 일 때
            # 거리 정보를 갱신해 준다.
            if new_cost < dist[n[0]]:
                dist[n[0]] = new_cost
                heapq.heappush(q, (n[0], new_cost))

    return dist

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))

    # 출발지, 목적지 2개에서 각각 다익스트라를 수행하여 각 노드들 간의 거리 정보를 구한다.
    startdijk = dijkstra(s, graph)
    n1dijk = dijkstra(a, graph)
    n2dijk = dijkstra(b, graph)

    # 세 배열을 합쳤을 때 가장 거리 합이 작은 노드, 즉 출발지점으로부터 경유지, 경유지로부터 목적지1, 경유지로부터 목적지2 의 거리 합이
    # 가장 짧은 거리 값이 정답이다.
    res = [0] * (n+1)
    for i in range(1, n+1):
        res[i] = startdijk[i] + n1dijk[i] + n2dijk[i]

    print(min(res[1:]))
    return min(res[1:])


solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])
