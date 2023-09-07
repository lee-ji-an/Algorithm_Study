## Info
[2146 다리 만들기](https://www.acmicpc.net/problem/2146)

## 💡 풀이 방법 요약
> BFS
1. board를 탐색하면서 1을 발견하면 각 구역에 대해 구역 number를 붙이고 visited를 True로 변경
    - 바깥 쪽에 있는 자리를 큐에 넣어서 반환 
2. 1번에서 반환받은 자리에서 시작해서 bfs 로 탐색하다가 다른 구역을 만나면 그 최솟값을 반환
3. 1, 2번을 전체 멥에 대해서 반복

## 🙂 마무리
https://www.acmicpc.net/board/view/32183