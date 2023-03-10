## Info
[17780 새로운 게임](https://www.acmicpc.net/problem/17780)

## 💡 풀이 방법 요약
> 흰색, 빨간색 칸에서 순서를 지키는 것과 파란색 칸에서 재귀호출 하는 부분에 유의하여 구현
- 각 `board` 칸은 `deque`로 만들어서 `append`와 `pop`을 효과적으로 수행할 수 있도록
  - 흰색 칸으로 이동할 때는 순서를 유지해야 하므로 `pop` -> `appendleft`
  - 빨간색 칸으로 이동할 때는 순서를 반전해야 하므로 `pop` -> `append`
- 옮겼을 때 한 칸에 있는 말 개수가 4개 이상이 되면 즉시 `return`

## 🙂 마무리
재귀호출의 리턴을 신경씁시다.