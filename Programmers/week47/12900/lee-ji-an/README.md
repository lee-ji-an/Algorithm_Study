## Info
[12900 2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900)

## 💡 풀이 방법 요약
> DP
`dp[i] = n 이 i일 때 타일 채우는 경우의 수
```Python
dp[i] = dp[i - 1] + dp[i - 2]

dp[i]의 경우의 수는...
dp[i - 1] + 세로 막대 추가
dp[i - 2] + 가로 막대 추
````

## 🙂 마무리

