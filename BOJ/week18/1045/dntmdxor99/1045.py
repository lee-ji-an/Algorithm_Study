import sys
import heapq
input = sys.stdin.readline


def my_par(x):
    while x != par[x]:
        x = par[x]
    return x


def union(x, y):
    par_x = my_par(x)
    while y != par[y]:
        temp, y = y, par[y]
        par[temp] = par_x
    par[y] = par_x


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [list(input().strip()) for _ in range(n)]

    pq = []
    for i in range(n):
        for j in range(i, n):
            if maps[i][j] == 'Y':
                heapq.heappush(pq, (i, j))      # start < end가 될 수 있도록 엣지를 파악함

    if len(pq) < m:     # 엣지의 개수가 m이하라면 답이 없는 것
        print(-1)
        exit(0)

    trash = list()      # 우선 mst를 만들고, 뒤에 남는 애들을 넣어야 함
    par = [*range(n)]
    answer = [0] * n

    cnt = 0
    while pq:
        i, j = heapq.heappop(pq)
        if my_par(i) != my_par(j):
            union(i, j)
            answer[i] += 1      # 바로 정답에 더함
            answer[j] += 1
            cnt += 1
        else:
            heapq.heappush(trash, (i, j))       # 남는 쓰레기들을 넣어야 함

    if cnt != n - 1:        # 만약 mst가 만들어지지 않았으면 답이 없는 것임
        print(-1)
        exit(0)

    for _ in range(m - cnt):
        i, j = heapq.heappop(trash)
        answer[i] += 1
        answer[j] += 1

    print(*answer, sep=' ')
