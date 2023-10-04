## Info
- [2638 치즈](https://www.acmicpc.net/problem/2638)

## 💡 풀이 방법 요약
> BFS

`초기 세팅`  
- visited : (0, 0)을 시작으로 BFS 탐색 -> 외부 공기와 접촉해 있는 장소를 표시  
- cheese : 녹지 않은 치즈를 집합으로 관리함 -> cheese에 '1'인 위치를 담음.

`치즈 녹이기`
1. cheese에 있는 위치를 모두 탐색
2. 상하좌우 탐색 -> 외부 공기와 접촉한 부분(visited == True)이 2개 이상이면 melting_cheese에 담음
3. 외부 공기와 접촉해 있는 곳 / cheese 갱신 (치즈는 초마다 한꺼번에 녹으므로 한 번에 연산해줘야 합)
4. cheese에 원소가 없을 때까지 반복


## 🙂 마무리
