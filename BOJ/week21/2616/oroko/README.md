## Info
[2616 소형기관차](https://www.acmicpc.net/problem/2616)

## 💡 풀이 방법 요약
> dp !!!

* dp[i][j]는 i번 기관차까지, j번 객차까지 봤을 때 운송할 수 있는 최대 손님 수
* sum은 j-limit ~ j번 객차에 타고 있는 손님 수의 최댓값
* dp[0][j] = max(dp[0][j-1], sum)
* dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + passenger[j], dp[i-1][j-limit] + sum)

## 🙂 마무리
이걸 하다니 디피 !!