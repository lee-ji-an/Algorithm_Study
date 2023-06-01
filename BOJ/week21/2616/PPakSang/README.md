## Info
[2616 소형기관차](https://www.acmicpc.net/problem/2616)

## 💡 풀이 방법 요약
> 한 기관차를 선택하면 그 뒤로 k 개가 자동 선택 -> 누적합
> 
> n 이하에서 어떤 수를 선택했을 때 최댓값 -> for i in range(1, 10): dp[i] = Math.max(num[i], dp[i-1])
> 
> k 개 골라야하면 (그 전 값과, 1개 고르고 k-1 개 골랐을 때) 값 비교
> 
> dp[j][k] = Math.max(dp[j+1][k], choose[j] + dp[j+constant][k-1]);

## 🙂 마무리

