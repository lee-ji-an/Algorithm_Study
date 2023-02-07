## Info

[10942 팰린드롬?](https://www.acmicpc.net/problem/10942)

<br>

## 💡 풀이 방법 요약

> P(i, j) = P(i+1, j-1) && arr[i] == arr[j]

1. dp[i][i] = true (길이가 1이면 팰린드롬)
2. 길이가 2일 때 팰린드롬인지 확인해서 저장
3. 길이가 k+1(2 <= k < N)일 때 점화식 활용해서 팰린드롬인지 확인
4. 질문마다 dp[S][E]를 출력

<br>

## 🙂 느낀 점
아직 점화식을 세우는게 쉽지 않다 구글링 함 ,,