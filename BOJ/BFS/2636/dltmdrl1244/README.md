## Info
[2636 치즈](https://www.acmicpc.net/problem/2636)

## 💡 풀이 방법 요약
- 구멍을 제외하고 공기랑 맞닿아 있는 부분이 녹는다 -> 치즈 외부에서 경계를 핥으면서 BFS
- 마침 주어진 보드의 가장자리는 무조건 치즈가 없다는 가정이 있으므로, 가장자리에서 BFS 시작하면 된다.
- 녹인 치즈의 면적을 구하고, 빼기 전에 현재 치즈 넓이를 저장해 놓고 0이 됐을 때 불러올 수 있도록 함
- 나머지는 일반적인 BFS와 동일
  
## 🙂 마무리
문제 조건을 잘 읽자.