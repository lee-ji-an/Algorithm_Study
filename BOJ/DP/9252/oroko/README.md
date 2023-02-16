## Info
[9252 LCS 2](https://www.acmicpc.net/problem/9252)

## 💡 풀이 방법 요약
> dp[i][j] = dp[i-1][j-1]+1 or max(dp[i-1][j], dp[i][j-1])

* LCS 와 같은 문제이다.
* 대신 parent를 기록해서 마지막에 LCS를 추적했다.

## 🙂 느낀 점
이걸 왜 그리 오랫동안 해내지 못한걸까 ...