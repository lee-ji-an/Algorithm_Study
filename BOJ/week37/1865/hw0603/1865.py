import sys

TC = int(sys.stdin.readline())

def solve(N, dist, graph) -> str:
    dist[1] = 0  # 시작노드

    for round in range(N):
        for node in range(1, N+1):
            for adjNode, adjCost in graph[node]:
                if (dist[adjNode] > dist[node] + adjCost):
                    if (round == N-1):
                        return "YES"  # N-1 번까지의 round 이후 더 돌면 음의 사이클 존재
                    dist[adjNode] = dist[node] + adjCost
    return "NO"


for test_case in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())  # 지점, 도로, 웜홀

    graph = [[] for _ in range(N+1)]
    dist = [sys.maxsize] * (N+1)  # idx 0 사용 X

    # 도로 데이터
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())  # 시작지점, 도착지점, 통과 소요 시간
        graph[S].append([E, T])
        graph[E].append([S, T])
    # 웜홀 데이터
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())  # 시작지점, 도착지점, 줄어드는 시간
        graph[S].append([E, -T])

    print(solve(N, dist, graph))
