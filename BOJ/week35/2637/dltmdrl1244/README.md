## Info
- [2637 장난감 조립](https://www.acmicpc.net/problem/2637)

## 💡 풀이 방법 요약
- (부품 A를 만드는 데 필요한 부품의 개수) x (B를 만들기 위해 필요한 A 수) 를 `부품 B를 만드는 데 필요한 부품의 개수` 배열에다가 더해나감으로써 상위 부품을 만들어 나감
- 이 때 위상 정렬을 이용해서 먼저 탐색해야 하는 모든 하위 부품들을 차례대로 탐색해야지만 정확한 요구 부품 수를 구할 수 있음
- indegree 감소시키고 0이면 큐에 넣는것은 다른 위상정렬 문제와 동일

## 🙂 마무리
