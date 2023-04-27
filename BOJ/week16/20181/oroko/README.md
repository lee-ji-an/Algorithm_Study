## Info
[20181 꿈틀꿈틀 호석 애벌레 - 효율성](https://www.acmicpc.net/problem/20181)

## 💡 풀이 방법 요약
> dp[k]는 (k-1)번째 먹이까지 먹었을 때의 최대 에너지

* sum은 현재 먹은 누적 만족도 (i번째부터 (j-1)번째 먹이까지 먹음)
* dp[k] : (k-1)번째 먹이까지 먹었을 때의 최대 에너지
  * sum >= K이면 dp[j] = Math.max(dp[j], dp[j] + sum - K)
  * sum < K이면 dp[j] = Math.max(dp[j], dp[j-1])

## 🙂 마무리
한 반복 내에서 두 포인터가 둘 다 변하게 하면 혼란 ,,

