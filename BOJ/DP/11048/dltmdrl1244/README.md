## Info
[11048 이동하기](https://www.acmicpc.net/problem/11048)

## 💡 풀이 방법 요약
> `N^2` 순차 탐색하면서 위, 왼쪽 칸 중 큰 값 + 본인 칸의 사탕 개수 더하는 작업 반복
- 어떤 칸 (i, j)까지 도달하는 데 먹을 수 있는 최대 사탕 개수는 `칸 (i-1, j)까지 도달하는 데 먹을 수 있는 최대 사탕 개수`와 
`칸(i, j-1)까지 도달하는 데 먹을 수 있는 최대 사탕 개수` 둘 중 큰 값에 칸(i, j)에 놓인 사탕 개수를 더한 값
- top-down 방식으로 N^2 순차 탐색하면서 dp 리스트를 채워 간다.

## 🙂 마무리