## Info
[1937 욕심쟁이 판다](https://www.acmicpc.net/problem/1937)

## 💡 풀이 방법 요약
DFS + DP로 풀이한다.  
이중 루프를 통해 방문하지 않은 모든 칸에 대하여 DFS 탐색(함수 호출)을 진행한다.  
  
`dfs()` 안에서는 재귀적으로 수행할 것이므로, 이미 방문한 지점에 대해서는 해당 칸의 dp값을 바로 리턴해 주고, 처음 방문하는 칸이라면 dp값을 1로 설정한다.  
현재 좌표 인근의 4방향 좌표 탐색을 진행하는데, 각 방향 중 현재 칸 보다 대나무 수가 많은 칸에 대해서만 재귀호출하여 탐색한다.  
주변에 현재 칸 보다 값이 큰 칸이 없으면 가장 깊게 들어온 것이므로 그 칸의 dp값을 반환하면 된다.  
`반환된 dp값+1` 과 `현재 dp값` 중 큰 값으로 갱신하고, `ans`변수도 갱신해 준다.  
  
루프 종료 이후 `ans` 출력하면 정답

## 🙂 마무리
