import heapq
import sys
input = sys.stdin.readline

N = int(input())

hq = []
sp_list = [[-1] * (N + 1) for i in range(N + 1)]
res_adj = [[]]
ans = 0


for i in range(N):
    row = list(map(int, input().split()))
    res_adj.append([0] + row)
    for j in range(i + 1, N):
        heapq.heappush(hq, (row[j], i + 1, j + 1))

for i in range(N + 1):  # 나 자신으로 향하는 루트의 거리는 0
    sp_list[i][i] = 0

flag = False
while len(hq) != 0:
    weight, v, w = heapq.heappop(hq)
    if sp_list[v][w] == weight:
        continue

    for node in range(1, N + 1):
        for node2 in range(1, N + 1):
            if sp_list[node][v] >= 0 and sp_list[w][node2] >= 0:
                distance = sp_list[node][v] + weight + sp_list[w][node2]
                if res_adj[node][node2] > distance:  # 정답 길이보다 더 작은 길이가 나오면 flag 체크 -> -1 출력
                    flag = True
                    break
                elif res_adj[node][node2] == distance:
                    sp_list[node][node2] = distance
                    sp_list[node2][node] = distance
    if flag:
        ans = -1
        break

    ans += weight

print(ans)
