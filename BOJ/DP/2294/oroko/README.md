## Info

[2294 동전 2](https://www.acmicpc.net/problem/2294)

<br>

## 💡 풀이 방법 요약

> dp[i] = min(dp[i], dp[i - coin] + 1)

1. 입력은 중복을 제거하기 위해 set으로 받는다.
2. dp 배열을 INF로 채운다.
3. dp[0] = 0
4. i - coin >= 0 이면 dp[i] = min(dp[i], dp[i-coin]+1)
   1. 정수 범위 때문에 dp[i-coin]이 INF가 아닐 때만 가능
5. dp[k] 출력 (INF이면 -1 출력)

<br>

## 🙂 느낀 점
1, 2, 3 더하기 4 문제랑 똑같다 !