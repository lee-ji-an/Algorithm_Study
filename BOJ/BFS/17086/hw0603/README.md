## Info
[17086 아기 상어 2](https://www.acmicpc.net/problem/17086)

## 💡 풀이 방법 요약
맵을 입력받으면서 상어 좌표를 미리 저장해 놓고, 큐의 초기 상태로 사용한다.(Multisource)  
큐의 길이를 기준으로 슬라이싱하여 `cnt`를 증가시키면서 인접 좌표들에 `cnt`값을 저장한다. 저장 시 이전의 최댓값과 계속 비교하여 최댓값을 유지시켜 주고, BFS 종료 이후에 최댓값을 출력하면 된다.  
상어 좌표의 값과 빈 칸의 값을 문제 범위 밖의 큰 수로 지정해 두고, 대소 관계를 통해 방문 체크를 하면 별도의 `visited` 배열 없이도 해결할 수 있다.

## 🙂 마무리
현재는 큐가 빌 때 까지 루프를 돌리는데, 모든 좌표가 다 마킹되어도 큐가 비지 않아 불필요한 연산이 더 생긴다.  
cnt값을 저장할 때 개수를 세서 맵 총 크기와 비교하면 조기 종료가 가능할 듯.
