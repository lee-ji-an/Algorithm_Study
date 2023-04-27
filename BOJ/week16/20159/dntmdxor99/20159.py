import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maps = list(map(int, input().split()))
    last = maps[-1]

    for i in range(1, n // 2):
        maps[i * 2] += maps[i * 2 - 2]
        maps[n - 1 - i * 2] += maps[n + 1 - i * 2]

    m = max(maps[1], maps[-2])

    for i in range(0, n - 2, 2):
        m = max(m, maps[i] + maps[i + 1] - last, maps[i] + maps[i + 3])
    print(m)
