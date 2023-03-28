## Info
[17404 RGB거리 2](https://www.acmicpc.net/problem/17404)

## 💡 풀이 방법 요약
`dp[i][j] = i번 집을 j색으로 칠했을 때, 첫 집부터 i번째 집을 칠하는 데 드는 최소 비용` 으로 정의한다.  
첫 집과 마지막 집도 색이 달라야 하므로, 첫 집의 색이 될 수 있는 모든 경우 3가지에 대해 조사하여 조건에 맞는 상황에서만 최솟값을 계산해야 한다.  
```python
# 현재 집을 칠하는 데 드는 비용 + 이때까지의 최솟값
    dp[house][cur_color] = cost[house][cur_color] + min(dp[house - 1][cand1], dp[house - 1][cand2])
```

## 🙂 마무리
첫 집이랑 마지막 집을 어떻게 처리해야 하는지 몰라서 검색의 힘을 좀 빌렸다..
