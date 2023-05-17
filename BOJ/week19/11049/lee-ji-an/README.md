## Info
[11049 행렬 곱셈 순서](https://www.acmicpc.net/problem/11049)

## 💡 풀이 방법 요약
> dp 를 이용하는 문제

dp 에 2차원 리스트를 이용

dp[i][j] ( i번째부터 j번째까지의 행렬 곱셈을 했을 때 곱셈 연산의 횟수 )
- i + 1 번째 지점을 기준으로 나눈 두 행렬을 곱했을 때 연산횟수
- i + 2 번째 지점 ~
- ....
- j - 1 번째 지점 ~
- j 번째 지점 ~  
-> dp[i][j] : 위의 연산 횟수를 모두 구한 후 그 중에서 제일 작은 연산횟수를 저장

## 🙂 마무리
 2차원 dp 리스트를 채워야하는데 한 원소를 채울 때 약 j - i 개만큼 을 보아야 해서 시간복잡도가 N^3이다.  
 그래서 Python3 로는 시간초과가 난다 🥲