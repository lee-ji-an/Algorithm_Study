import sys
input = sys.stdin.readline

N = int(input())

price_list = [[] for _ in range(N)]
dp_list = [[float('inf')] * 9 for _ in range(N)]  # r-r, r-g, r-b, g-r, g-g, g-b, b-r, b-g, b-b

for i in range(N):
    price_list[i] = list(map(int, input().split()))


def dp(num):
    ans = float('inf')

    for i in range(3):  # 처음 집 값 설정
        dp_list[0][i * 3 + i] = price_list[0][i]
    for n in range(1, num):
        for i in (0, 3, 6):
            for j in range(3):
                dp_list[n][i + j] = min(dp_list[n - 1][i + (j + 1) % 3], dp_list[n - 1][i + (j + 2) % 3])\
                                    + price_list[n][j]

    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            ans = min(dp_list[N - 1][i * 3 + j], ans)

    return ans


print(dp(N))
