import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    costs = list(map(int, input().split()))
    m = int(input())
    dp = [-float('inf') for _ in range(m + 1)]

    for y in range(n - 1, -1, -1):
        cost = costs[y]     # 값을 받아옴
        for x in range(cost, m + 1):        # 해당 방 번호의 값 이후로만 살 수 있음
            dp[x] = max(y * int('1' * (x // cost)), dp[x], dp[x - cost] * 10 + y)      # 높은 숫자로 일단 꽉 채운 값, 기존 값, 한 개만 넣었을 때의 값

    print(dp[m])