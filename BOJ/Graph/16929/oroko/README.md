## Info

[16929 Two Dots](https://www.acmicpc.net/problem/16929)

<br>

## 💡 풀이 방법 요약

> dfs로 cycle 있는지 확인하고 하나라도 찾으면 그만하기

### Pos
* x좌표와 y좌표
* 이동하기 전 좌표

### dfs
1. 4개 이상 거쳐서 재방문 했으면 true 반환
2. 같은 색깔이고 이전 좌표가 아니면 다음으로 이동
3. cycle인거 발견했으면 그만

<br>

## 🙂 느낀 점
이전 노드로 되돌아가지만 않으면 되는 로직 + dfs + 찾으면 그만가도록 