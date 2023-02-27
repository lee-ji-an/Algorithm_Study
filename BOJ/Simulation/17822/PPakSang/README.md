## Info

[17822 원판돌리기](https://www.acmicpc.net/problem/17822)

## 💡 풀이 방법 요약

1. 밀기
> 1차원 배열 n 번 밀기
> 
> [1, n] 에는 [M - n + 1, M] 의 수를 넣고
> 
> [n+1, M] 에는 [1, n] 의 수를 넣는다
> 
> 역방향으로 n 번 밀기는 M - n 번 순방향 밀기와 같다

2. 지우기
> 사방 탐색으로 같은 숫자가 있는 경우 삭제

3. 덧셈/뺄셈
> 전체 탐색 2번 (평균 구하기, 덧셈/뺄셈)
## 🙂 느낀 점