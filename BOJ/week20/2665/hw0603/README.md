## Info
[2665 미로만들기](https://www.acmicpc.net/problem/2665)

## 💡 풀이 방법 요약
BFS + heapq로 플이한다.  
BFS 노드는 `(벽을 부순 횟수, row, col)` 로 저장하여 벽을 부순 횟수(=비용)가 낮은 노드들이 먼저 처리되도록 한다.  
큐에서 `pop`했을 때 목적지에 도착했다면 그 당시의 벽을 부순 횟수를 출력하면 된다.


## 🙂 마무리
벽 부수고 이동하기 시리즈의 하위호환 문제(?)  
처음에는 `visited`를 "가장 최근 방문했을 때 벽을 부순 횟수"로 정의하고, 초깃값을 `sys.maxsize`로 잡은 뒤,
```python
if (visited[nr][nc] > cnt):
    if (room[nr][nc] == 0):
        visited[nr][nc] = cnt+1
        heapq.heappush(q, (cnt+1, nr, nc))
    else:
        visited[nr][nc] = cnt
        heapq.heappush(q, (cnt, nr, nc))
```
이와 같이 현재 노드보다 이전에 벽을 더 많이 깬 채로 방문했을 경우 대소비교를 통해 다시 방문하여 값을 갱신하는 방법으로 풀이했었는데, 생각해 보니 `heapq`를 사용하므로 항상 시간이 지날수록 벽을 부순 횟수가 큰 노드가 들어오는 것이 보장되므로 별도로 관리해 줄 필요가 없었다.  
따라서, `visited`를 `bool` 형태로 변경하여 다시 제출했다.
