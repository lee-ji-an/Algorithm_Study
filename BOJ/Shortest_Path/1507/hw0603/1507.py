import sys

N = int(sys.stdin.readline())
dist = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

path = [[True]*N for _ in range(N)]  # 도시 i에서 도시 j로 가는 경로가 존재할 경우 True. 초깃값은 모든 간선이 존재한다고 가정

# 플로이드 와샬 알고리즘을 역으로 활용함 (i, j, k 중 어느 쌍이라도 같으면 안 됨)
for k in range(N):
    for i in range(N):
        if (i == k):
            continue
        for j in range(N):
            if (i == j or k == j):
                continue

            # 구해 놓은 거리의 최솟값이 k도시를 거쳐 가는 경우와 같다면 i와 j 사이에 직접 연결되는 도로는 없는 것
            if (dist[i][j] == dist[i][k]+dist[k][j]):
                path[i][j] = False
            # 지금 보고 있는 경로(k도시를 경유하는 경로)보다 인풋으로 들어온 최소 경로가 더 클 경우 (불가능한 경우)
            elif (dist[i][j] > dist[i][k]+dist[k][j]):
                sys.exit(print(-1))

result = 0
for i in range(N):
    for j in range(i, N):
        # 경로가 존재하는 경우 가중치를 누적
        if (path[i][j]):
            result += dist[i][j]

print(result)
