## Info
[1414 - 불우이웃돕기](https://www.acmicpc.net/problem/1414)

## 💡 풀이 방법 요약
> Minimum Spanning Tree 구현
- 각 컴퓨터를 모두 연결하고 남은 랜선을 기부하는데 기부할 수 있는 랜선의 최대 길이를 구한다는 것은 각 컴퓨터를 최소 비용으로 연결해야 한다는 뜻 -> MST 구현
- 크루스칼 알고리즘을 통해 MST 구현, MST에 포함되지 않는 간선은 기부, 즉 `answer`에 더함

## 🙂 마무리
끝