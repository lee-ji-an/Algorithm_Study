## Info
[1799 비숍](https://www.acmicpc.net/problem/1799)

## 💡 풀이 방법 요약
N Queen과 유사한 문제. 백트래킹을 활용해서 풀이한다.  
비숍은 대각선 방향으로만 이동하므로, 대각선을 기준으로 충돌 여부를 검사하면 된다.  
  
우상향 대각선은 `row+col`이 `diagIdx`로 일정하고,  
우하향 대각선은 `col-row`가 `diagIdx`로 일정하다.
  
우상향 대각선을 따라 비숍을 하나씩 놓고, 우하향 대각선에서 충돌하는 것이 있는지 확인하면서 백트래킹한다.

## 🙂 마무리
풀이 참고해서 단순 백트래킹으로 풀었는데 매우 느리다.  
최적화 풀이는 이해가 잘 안 간다..
