## Info
[14391 종이조각](https://www.acmicpc.net/problem/14391)

## 💡 풀이 방법 요약
> (구글링했음) 비트마스크 이용
- 총 n*m 개의 각 칸에 0 또는 1을 할당해 주는 경우를 모두 고려하기 위해 `2^(n*m)`의 숫자 사용
- 각 칸에서 0이면 세로방향, 1이면 가로방향으로 진행. 다른 방향으로 진행하는 칸을 만나면 점수에다 더함
- 먼저 가로방향을 먼저 고려하여 row, col 순서대로 가로방향이면 숫자 더하여 진행, 세로방향이면 지금까지 구한 값 더해감
- 세로방향도 똑같이 진행

## 🙂 마무리
처음에는 가로로 죽죽 세로로 죽죽 그은게 가장 클 줄 알았는데 당연히 예외가 있었고... 가로진행/세로진행/스탑 세가지 경우의 수를 따져가며 그래프탐색으로 풀려고 했지만 구현이 쉽지 않았다. 결국 구글링해서 비트마스크 풀이를 찾았고 이해 완료 했다.