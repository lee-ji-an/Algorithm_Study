import time
if __name__ == "__main__":
    n = int(input())
    maps = [True] * (n + 1)
    maps[0] = maps[1] = False

    for i in range(2, int((n) ** 0.5) + 1):     # 에라토스테네스의 체로 소수인 애들 미리 파악함(소수는 maps에서 True)
        if maps[i]:
            for j in range(i * 2, n + 1, i):
                maps[j] = False

    left, right = 2, 3      # 둘 다 좌측부터 시작함
    total = 5       # 지금까지의 합
    ans = 0

    while left < right < n:     # n이 소수인지 아닌지는 나중에 파악함, left == right == n이 소수면 +1해서 답함
        if total >= n:
            if total == n:
                ans += 1

            # 크거나 같으므로 left를 옮겨서 total을 줄여야 함
            total -= left
            for i in range(left + 1, right + 1):
                if maps[i]:
                    left = i
                    break

        elif total < n:     # total이 작다면 right를 옮겨서 total을 크게 만들어야 함
            for i in range(right + 1, n):
                if maps[i]:
                    right = i
                    total += i
                    break

    print(ans + 1 if maps[n] else ans)
