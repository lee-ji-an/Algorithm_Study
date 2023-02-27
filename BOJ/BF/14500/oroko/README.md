## Info

[14500 테트로미노](https://www.acmicpc.net/problem/14500)

<br>

## 💡 풀이 방법 요약

> dfs로 테트로미노를 놓아보고 다 놓으면 max 갱신하기

### put(...)
* 상하좌우로 뻗어나가면서 4칸 놓기
* T 모양 테트로미노는 따로 처리해야 함
  * 상하좌우가 3개 이상이면 현재 칸을 기준으로 상하좌우의 합에서 상하좌우 중 최솟값 빼기

<br>

## 🙂 느낀 점
그냥 bfs나 dfs를 하면 T 모양은 탐색 못하는구나를 알게 되었다.