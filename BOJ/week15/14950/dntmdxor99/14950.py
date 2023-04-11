import sys
import heapq
input = sys.stdin.readline


def my_par(x):      # 내 부모를 찾음
    while x != par[x]:
        x = par[x]
    return x


def union(x, y):        # 합침
    par[my_par(y)] = my_par(x)


if __name__ == "__main__":
    n, m, t = map(int, input().split())
    par = [*range(n + 1)]
    maps = []
    ans = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        heapq.heappush(maps, [c, a, b])

    i = 0
    while maps:
        c, a, b = heapq.heappop(maps)
        if my_par(a) != my_par(b):
            union(a, b)
            ans += c + i * t
            i += 1

    print(ans)
