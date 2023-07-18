## Info
[7579 앱](https://www.acmicpc.net/problem/7579)

## 💡 풀이 방법 요약
냅색 문제의 응용 버전  
`메모리`는 냅색의 `무게`에 해당하고, `비용`은 냅색의 `가치`에 해당한다.  
이때, 냅색에서는 일정 무게 이하에서의 최대 가치를 구하지만, 이 문제에서는 일정 메모리를 넘으면서 최소 비용을 구하는 문제라고 할 수 있다.  
  
`dp[i][j] = i번째 앱까지 조사했을 때, 비용 j로 확보할 수 있는 최대의 메모리` 로 정의한다.  
앱과 비용을 기준으로 이중 루프를 순회하며 다음을 수행한다.
1. 현재 앱의 비용이 j보다 큰 경우
   - 현재 앱은 끌 수 없으므로 이전 dp값을 그대로 가져 온다(`dp[i-1][j]`)
2. 현재 앱의 비용이 j 이하인 경우
   - 현재 앱을 끈 뒤의 메모리와 끄지 않을 경우의 메모리 중 큰 값을 취한다.
   - `max(memory[i] + dp[i-1][j-cost[i]], dp[i-1][j])`

dp 테이블을 완성한 다음, `dp[N][index]` 가 처음으로 M보다 커지는 경우의 `index` 값을 출력하면 되는데, 이때는 이진 탐색을 활용하여 구한다.

## 🙂 마무리
None