import sys

N = int(sys.stdin.readline())
MOD = 1000000000

dp = [[0 for _ in range(1 << 10)] for _ in range(10)]  # dp[lastnum][bitmask]: 비트마스크로 0~9의 숫자가 사용됐는지를 마킹

# 1~9까지 lastnum 별로 비트 켜기(초기화)
for lastnum in range(1, 10):
    dp[lastnum][1 << lastnum] = 1

# 한 번 순회할 때 마다 길이가 i인 경우를 모두 조사
for l in range(1, N):
    # 각 자릿수에서의 정보를 담을 배열
    dp_next = [[0 for _ in range(1 << 10)] for _ in range(10)]


    # dp 배열을 모두 순회하며 각 수의 뒷자리에 올 수 있는 수를 추가
    # 0 ~ 9까지 순회
    for lastnum in range(10):
        # 모든 비트를 순회
        for bit in range(1 << 10):
            # 0과 9는 각각 +1/-1 밖에 붙일 수 없음
            if (lastnum < 9):
                dp_next[lastnum][bit | (1 << lastnum)] = (
                    dp_next[lastnum][bit | (1 << lastnum)] + dp[lastnum + 1][bit]
                ) % MOD
            if (lastnum > 0):
                dp_next[lastnum][bit | (1 << lastnum)] = (
                    dp_next[lastnum][bit | (1 << lastnum)] + dp[lastnum - 1][bit]
                ) % MOD

    dp = dp_next

print(sum(dp[i][0b_0011_1111_1111] for i in range(10)) % MOD)  # lastnum=0~9 에 대해 비트가 모두 켜진 경우의 개수 합산
