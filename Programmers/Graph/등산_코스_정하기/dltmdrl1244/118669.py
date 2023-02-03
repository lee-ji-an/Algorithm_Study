import heapq

def dijkstra(graph, gates, summits):
    dist = [float('inf')] * len(graph)
    q = []
    # 각 출발지는 경로의 intensity가 0이므로 dist에 0 저장, 그리고 각 출발지에 인접해 있는 노드들을 PQ에 먼저 저장
    for gate in gates:
        for n_node, n_cost in graph[gate]:
            heapq.heappush(q, [n_cost, n_node])
        dist[gate] = 0

    while q:
        c_cost, c_node = heapq.heappop(q)
        # intensity가 더 작아질 수 없으면 필요 x
        if dist[c_node] <= c_cost:
            continue
        # c_node까지 가는 최소 intensity는 c_cost로 확정
        dist[c_node] = c_cost

        # 꼭대기까지 갔으면 거기서 다른 노드로 더 갈 수가 없음
        if c_node in summits:
            continue

        # 현재 노드와 인접해 있는 길을 발견함으로써 인접 노드들까지의 intensity를 줄일 수 있는 경로가 있으면 PQ에 push
        for n_node, n_cost in graph[c_node]:
            if dist[n_node] <= c_cost:
                continue
            heapq.heappush(q, [max(n_cost, c_cost), n_node])

    return dist


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    # 간선 저장
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))


    summits.sort()
    answer = [0, float('inf')]
    # 다익스트라로 출발지들로부터 각 목적지까지의 intensity들 중 최솟값을 구함
    dist = dijkstra(graph, gates, summits)

    # 가장 intensity가 작은, 작은경로가 여러개라면 그중 꼭대기 번호가 가장 작은 경로를 answer에 저장
    for summit in summits:
        if dist[summit] < answer[1]:
            answer = summit, dist[summit]

    return answer


# solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
# solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
# solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])
# solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5])