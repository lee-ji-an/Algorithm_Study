## Info
[1799 비숍](https://www.acmicpc.net/problem/1799)

## 💡 풀이 방법 요약
> 백트래킹

1. 대각선마다 하나씩 놓을 수 있음 (오른쪽 위로 향하는 대각선, 오른쪽 아래로 향하는 대각선)
    - 오른쪽 위로 향하는 대각선 -> row, col 합이 일정
    - 오른쪽 아래로 향하는 대각선 -> row, col 차가 일정
2. 오른쪽 위로 향하는 대각선을 기준으로 하나씩 놓음
   - 오른쪽 아래로 향하는 대각선에 겹치는 게 없는지 확인

```Python
dfs(n, cnt) : n = n번째 대각선, cnt = 비숍을 놓은 갯수
```


## 🙂 마무리
