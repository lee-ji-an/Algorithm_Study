import sys
input = sys.stdin.readline


def one_dp():
    n, m = map(int, input().split())
    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    dp = [sys.maxsize] * m

    for i in range(m):
        if memory[0] >= i:
            dp[i] = cost[0]

    temp = dp.copy()

    for i in range(1, n):
        for j in range(m):
            if memory[i] >= j:  # i번째 프로세스가 사용 중인 메모리를 빼면 j 메모리를 사용하는 프로세스를 넣을 수 있음
                temp[j] = min(dp[j], cost[i])
            else:
                temp[j] = min(dp[j], dp[j - memory[i]] + cost[i])

        dp = temp.copy()

    print(dp[m - 1])


def recur(n, re_m, c):
    global dp
    if re_m <= 0:       # 메모리가 확보되면 지금까지의 cost를 반환함
        return c

    elif n == -1:        # 메모리가 확보되지 않고, 끝까지 갔다면 maxsize를 반환함
        return sys.maxsize

    lvalue = dp.get((n - 1, re_m), recur(n - 1, re_m, c))
    rvalue = dp.get((n - 1, re_m - memory[n]), recur(n - 1, re_m - memory[n], c + cost[n]))

    dp[(n, re_m)] = min(lvalue, rvalue)

    return dp[(n, re_m)]


if __name__ == "__main__":
    n, m = map(int, input().split())
    # pair = sorted(zip(list(map(int, input().split())), list(map(int, input().split()))), key = lambda x: (x[1], x[0]))
    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    dp = dict()

    print(recur(n - 1, m, 0))