## Info

[16234 인구 이동](https://www.acmicpc.net/problem/16234)

<br>

## 💡 풀이 방법 요약

> bfs로 연합인 나라를 모두 찾고 인구수 갱신 -> 변화가 없을 때까지 반

1. 큐에 전체 위치를 모두 넣음
2. 큐의 길이를 재서 큐의 길이만큼 검사해서 1일차, 2일차, .. 나눠서 검사 (이때 visited는 day를 저장하고 현재 day 보다 작은 수가 들어있으면 검사)
3. 인구를 갱신할 때 갱신한 위치를 큐에 넣어서 다음 번에 갱신한 위치만 연합국 검사


<br>

## 🙂 느낀 점
처음에는 모든 위치 검사하다가
인구 갱신한 위치만 검사하니까 엄청 빨라졌다 !