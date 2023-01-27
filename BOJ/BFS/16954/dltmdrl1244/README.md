## Info
[링크](https://www.acmicpc.net/problem/16954)

## 💡 풀이 방법 요약
> 한 회차의 탐색이 모두 끝나면 다음 회차의 탐색이 시작되는 BFS의 특성을 이용

- 일반적인 BFS를 수행하되 회차 정보를 저장하고 있음. 큐에 `append` 할 때는 `회차+1`을 넣어준다.
- 그리고 전역 변수로 현재 탐색하고 있는 회차를 기록하고, 더 큰 값이 `pop`되었으면 이제 다음 회차를 탐색할 차례이므로 `visited`와 `board`를 한 칸씩 움직인다.

## 🙂 마무리
`visited`도 함께 움직여야 한다는 사실을 알아내기까지가 시간이 많이 소요됐다..