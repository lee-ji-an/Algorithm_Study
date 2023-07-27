## Info
- [3197번 백조의 호수](https://www.acmicpc.net/problem/3197)

## 💡 풀이 방법 요약
> BFS

하나의 백조에서 시작해서 BFS를 시행해 다른 백조를 만나면 종료

1. find_swan 함수 (백조가 만날 수 있는지 확인하는 함수)
- next_q 를 정의 = 다음 날에 사용할 큐
- 얼음을 만나면 -> 지금은 얼음이지만, 다음 날에 물이 될 곳 -> next_q 에 append
- 물을 만났을 때 -> 물이니까 얼음을 만날 때까지 계속 탐색해봐야 함 -> q에 append

2. melt 함수 (얼음을 녹이는 함수)
- next_q 를 정의 = 다음 날에 사용할 큐
- 처음에는 물인 부분을 모두 q에 넣고 시작
- bfs 탐색하면서 새롭게 물로 바꾼 곳을 next_q에 넣음 (새로 물로 바꾼 곳은 얼음과 맞닿아 있는 곳이므로 )

## 🙂 마무리
주의할 점..
```Python
    if lake[mv_r][mv_c] == 'X':
        next_q.append((mv_r, mv_c))
    else:
        q.append((mv_r, mv_c))
    visited[mv_r][mv_c] = True
```
next_q 에 넣은 장소도 큐에 넣음으로써 다음에 탐색하는 것이 확정된 상태 -> visited 체크를 해줘야 함