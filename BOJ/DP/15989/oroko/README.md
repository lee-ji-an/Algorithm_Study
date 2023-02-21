## Info

[15989 1, 2, 3 더하기 4](https://www.acmicpc.net/problem/15989)

<br>

## 💡 풀이 방법 요약

> dp[i] 는 i를 만들 수 있는 경우의 수, dp[j] += dp[j-i]

1. dp[0] = 1
2. 1로만 만들 수 있는 경우의 수를 dp[j]에 저장 (1 <= j <= n) => dp[j] += dp[j-1]
3. 1과 2로 만들 수 있는 경우의 수를 dp[j]에 더하기 => dp[j] += dp[j-2]
4. 1,2,3으로 만들 수 있는 경우의 수를 dp[j]에 더하기 => dp[j] += dp[j-3]
5. dp[n] 출력하기

<br>

## 🙂 느낀 점
숫자 j를 1, 2, 3으로 만들 수 있는 경우의 수를 모두 만들어 놓고 j+1을 구하면 중복으로 더하게 된다 !!