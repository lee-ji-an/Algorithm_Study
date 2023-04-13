import sys
import heapq
input = sys.stdin.readline


def my_par(x):      # 내 부모를 찾음
    while x != par[x]:
        x = par[x]
    return x


def union(x, y):        # 합침
    par_x = my_par(x)
    while y != par[y]:
        temp, y = y, par[y]
        par[temp] = par_x
    par[y] = par_x


if __name__ == "__main__":
    n, m, t = map(int, input().split())
    ans = (n - 2) * (n - 1) * t // 2
    par = [*range(n + 1)]
    maps = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        heapq.heappush(maps, [c, a, b])

    i = 0
    while i < n - 1:
        c, a, b = heapq.heappop(maps)
        if my_par(a) != my_par(b):
            union(a, b)
            ans += c
            i += 1

    print(ans)
