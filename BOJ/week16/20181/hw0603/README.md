## Info
[20181 꿈틀꿈틀 호석 애벌레 - 효율성](https://www.acmicpc.net/problem/20181)

## 💡 풀이 방법 요약
기본적으로 `left`~`right` 범위의 합이 K보다 클 때까지 `right`를 1씩 증가시킨다.  
구간 합이 K 이상이 되면 `left`를 증가시켜 구간을 줄인다.  
  
`dp[right] = max(dp[right], dp[right-1])`으로 `dp[i]`에 `i`까지 조사했을 때 에너지의 최댓값을 유지하고,  
left 전진 시에는  
`dp[right] = max(dp[right], dp[left-1] + partsum - K)`으로
(`left` 지점까지 에너지 최댓값+투포인터 사이의 최댓값) 과 현재의 최댓값을 비교하여 최댓값을 갱신해 준다.
  
`left == right` 이고 `partsum >= K` 인 경우에는 한 먹이의 크기가 `K`보다 큰 경우이므로 다음 먹이에서부터 새로 시작한다.


## 🙂 마무리
투 포인터에 DP인건 알겠는데 구현에서 막혀서 풀이를 좀 참고했다..

