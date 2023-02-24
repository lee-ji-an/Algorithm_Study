## Info
[17822 원판 돌리기](https://www.acmicpc.net/problem/17822)

## 💡 풀이 방법 요약
> 차근차근 해봅니다 ㅠㅠ

* plate[i][j]
  * i번째 원판의 j번째 수
  * 1 <= i <= N, 0 < j < M
* plates를 갱신할 때마다 sum과 cnt를 갱신한다.
  * increase(), decrease()
  * 평균을 바로 구하기 위함
* rotate()
  * 큐를 이용해서 회전한다.
* erase()
  * bfs로 인접한 수를 지운다.
  * 양 끝도 양쪽 다보기 주의
  * 지운 수가 없으면 false, 있으면 true 반환
* erase가 false인 경우 arrange()
  * 평균보다 작으면 +1, 크면 -1 해주기
  * sum, cnt 초기화하기

## 🙂 느낀 점
아이고 복자배라 .. 다양하개 양방향 연결리스트, 덱 해보다가 결국 순정으로 돌아왔다 !