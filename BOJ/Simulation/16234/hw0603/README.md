## Info
[16234 인구 이동](https://www.acmicpc.net/problem/16234)

## 💡 풀이 방법 요약
먼저 그래프 전체를 BFS탐색하여 모든 연합을 찾은 뒤, `day`를 증가시키면서 조건에 맞게 인구 이동을 진행한다.
연합이 더 이상 형성될 수 없을 때(인구 이동이 없을 때) 루프를 탈출하고, 그 시점의 `day`를 출력하면 정답.


## 🙂 마무리
정직하게 시키는 대로 풀었는데 엄청 느렸다. 메인 `while` 루프 안에서 `visited`를 매 번 초기화 해서 그런가 싶어 `day`의 대소를 기준으로 방문체크를 해 봤는데, 더 느려졌다..
