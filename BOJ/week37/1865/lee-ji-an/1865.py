import sys
input = sys.stdin.readline

TC = int(input())


def bellman_ford(start):
    dist = [10001] * (N + 1)
    dist[start] = 0
    for i in range(N):
        for s, e, cost in edge:
            if dist[s] + cost < dist[e]:
                dist[e] = dist[s] + cost
                if i == N - 1:
                    return True

    return False


for t in range(TC):
    N, M, W = map(int, input().split())
    road = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    edge = set()
    # 간선을 road에 저장, 중복된 간선이 있다면 더 작은 간선만 저장
    for m in range(M):
        S, E, T = map(int, input().split())
        if road[S][E] > T:
            road[S][E] = T
        if road[E][S] > T:
            road[E][S] = T
    for w in range(W):
        S, E, T = map(int, input().split())
        if road[S][E] > -T:
            road[S][E] = -T

    # 간선을 edge에 모두 저장
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            if road[s][e] != float('inf'):
                edge.add((s, e, road[s][e]))

    # Bellman ford 로 음수 간선이 있는지 검사
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
