## Info
[17822 원판 돌리기](https://www.acmicpc.net/problem/17822)

## 💡 풀이 방법 요약
원판 하나를 deque로 표현
1. 시계방항으로 회전 -> pop, appendleft
2. 반시계방향으로 회전 -> popleft, append

상하좌우에 대해서 숫자가 같은지 확인해서
같다면 set에 집어넣음
set에 있는 것은 모두 0으로 초기화

바꾼 게 없으면 숫자 갱신


## 🙂 마무리

