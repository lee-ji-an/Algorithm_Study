## Info
[5430 AC](https://www.acmicpc.net/problem/5430)

## 💡 풀이 방법 요약
- 하나의 배열을 그대로 넣은 덱과 반대로 넣은 덱을 사용
- R을 만날 때마다 cur을 증가시키면서 지금 배열 상태가 뒤집혀있는지 아닌지를 표시
- 뒤집혀 있다면 q2에서 popleft, 아니면 q1에서 popleft. 똑같이 유지해주기 위해 반대편에는 pop

## 🙂 마무리
