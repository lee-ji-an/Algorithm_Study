## Info

[16928 뱀과 사다리 게임](https://www.acmicpc.net/problem/16928)

<br>

## 💡 풀이 방법 요약

> bfs로 탐색하기

1. trap 배열에 인덱스:출발, 값:도착 저장하기
2. bfs로 탐색해서 가장 먼저 도착했을 때의 횟수 구하기

### bfs
1. 큐에 1 넣고, 1을 방문한 채로 시작
2. 100에 도착했으면 횟수 반환
3. 1~6까지 던져보고
   1. 100 넘으면 패스
   2. 트랩(사다리 또는 뱀)이면 타고 이동
   3. 다음 갈 곳이 방문한 적 없으면 방문 표시 하고 큐에 넣기

<br>

## 🙂 느낀 점
이번에는 큐에 넣기 전에 visited를 표시하는 방법으로 풀어봤다!<br>
최근에 풀었던 문제라서 1트만에 성공 ㅎㅎ
