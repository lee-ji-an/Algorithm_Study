## Info
[9663 N-Queen](https://www.acmicpc.net/problem/9663)

## 💡 풀이 방법 요약
![Lec12_back_tracking-7](https://user-images.githubusercontent.com/31981462/221578120-7269167c-a21e-4f6a-9dc4-73305fde3e81.jpg)
알고리즘 1 백트래킹 파트에서 배웠던 로직을 그대로 사용했다.  
Queen의 특성 상 한 row에는 두 개 이상의 퀸이 올 수 없으므로, `Q[i] = i번째 row에는 몇 번째 col에 Queen이 존재하는가?`로 정의한다.  
1. outer loop에서는 0열~N열까지 순회한다.
2. inner loop에서는 0행~현재 data가 존재하는 행까지 순회한다.
3. 올바른 퀸의 배치임을 나타내는 플래그인 `legal`을 T/F로 변경해 가면서 `legal`한 `j`를 찾은 경우 재귀호출하고, 호출 후에는 다른 `legal`한 `j`를 찾기 위해 방금 마킹한 곳을 `pop()` 한다.

## 🙂 느낀 점
C++기준 10초, Python3 기준으로는 10*3+2=32초...의 어마어마한 시간 제한을 가진 문제다.  
배운 대로 풀었는데 Python3으로는 TLE로 통과하지 못했고, PyPy로 제출하니 12초 가량으로 겨우 맞았다.  
~~이번엔 반칙 좀 쓸게..~~
