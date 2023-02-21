## Info

[2294 동전 2](https://www.acmicpc.net/problem/2294)

<br>

## 💡 풀이 방법 요약

> 동전을 고려하는 개수를 늘려주면서 2차원 dp같은 효과를 낸다
- 한 동전으로 표현할 수 있는 방법을 모두 구해놓고, 그 다음 동전으로 표현할 수 있는 새로운 방법을 모두 구해서 덮어씌우는 방식으로 중복을 제거
- 예를 들어 `1 동전`, `5 동전`으로 `7`원을 만든다고 하였을 때 먼저 `1원으로 1 ~ 7원을 만들 수 있는 방법 수(1)`을 미리 다 구해놓고
- 그 다음에 `5 동전`에 대해 '6원은 5원 + `dp[1]`' '7원은 5원 + `dp[2]`' 로 구함으로써 1+5, 5+1 등을 중복해서 보지 않을 수 있다.

<br>

## 🙂 느낀 점
8달 전의 이승기 풀이와 100% 일치함...;;