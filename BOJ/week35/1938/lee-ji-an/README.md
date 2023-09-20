## Info
- [1938 통나무 옮기기](https://www.acmicpc.net/problem/1938)

## 💡 풀이 방법 요약
> BFS

1. 현재 통나무의 상태를 (중심의 행 위치, 중심의 열 위치, 통나무의 방향(T, F)) 으로 판단
2. 시작 위치, 최종 위치에 해당하는 세 지점을 모두 리스트에 담음
3. 세 위치를 검사해서 시작 위치, 최종 위치의 방향을 구함.
4. 시작 위치에서 시작해서 최종 위치에 도달할 때까지 bfs 수행
   - bfs에 사용되는 q에 (row, col, direction, cnt) 형태로 집어넣음
   - (row, col, direction) 형태를 set에 넣어서 visited 체크
   - U, D, L, R 는 일반 bfs처럼 사방 탐색을 실시  
     -> 해당 위치에 통나무를 놓을 수 있다면 q, visited에 해당 경우를 넣음.
   - T 는 해당 위치에 통나무를 놓을 수 있다면 q, visited에 direction에 not 연산을 취해서 해당 경우를 넣음.  

## 🙂 마무리
#### 초기 코드에서 틀렸던 점
```Python
# 수정 전
visited.add((mv_r, mv_c, direction))
if check(mv_r, mv_c, direction):
    q.append((mv_r, mv_c, direction, cnt + 1))

# 수정 후
if check(mv_r, mv_c, direction):
    visited.add((mv_r, mv_c, direction))
    q.append((mv_r, mv_c, direction, cnt + 1))
```
수정 전 코드에서는 visited에 저장되어있지 않으면 그 즉시 현재 상태를 visited에 넣었다.

`안되는 이유`  

1. r, c 위치에서 세로 -> 가로로 회전하는 것
2. 이미 가로인 상태에서 위치만 한 칸 이동해서 r, c에 위치하는 것  

두 동작이 결과는 같더라도 1번 동작의 경우에는 불가능, 2번 동작의 경우에는 가능할 수 있음.  
따라서, `if check(...)` 이전에 visited에 넣으면 위 경우 때문에 모든 경우의 수가 탐색이 되지 않음