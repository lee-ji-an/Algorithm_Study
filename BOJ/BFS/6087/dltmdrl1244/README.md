## Info
[6087 레이저 통신](https://www.acmicpc.net/problem/6087)

## 💡 풀이 방법 요약
> 이전 이동 정보를 기록하여 커브를 도는 횟수를 계산

- 이전 이동 정보를 기록해가며 BFS 수행
- 이전 이동 정보와 다른 방향 (수직, 수평)으로 이동했다면 커브를 돈 것이므로 커브 횟수 + 1
- 이 때 같은 지점에 더 적은 커브를 돌면서 방문할 수 있으므로, 이전 값보다 작아질 수 있는 경우에 큐에 넣음


## 🙂 마무리
레이저 경로에 거울을 설치한다 → 커브 라는 생각이 조금은 어려울 수 있다