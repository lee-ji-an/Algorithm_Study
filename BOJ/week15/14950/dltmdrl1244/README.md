## Info
[14950 정복자](https://www.acmicpc.net/problem/14950)

## 💡 풀이 방법 요약
최소 신장 트리(Minimum Spanning Tree) 를 구성하는 문제
- 최소 신장 트리를 구성하는 알고리즘에는 프림 알고리즘과 크루스칼 알고리즘이 있고 본 문제는 프림으로 풀어야 함
    - 그 이유는 내가 정복한 나라들에 인접한 나라들만 이어서 정복할 수 있으므로 spanning tree를 확장시켜 나가야 하기 때문
    - 반면 크루스칼의 경우, 간선의 노드가 mst에 속하는지 여부는 고려하지 않고 비용이 작은 간선을 먼저 탐색하기 때문
- 나머지는 평범한 프림 알고리즘

## 🙂 마무리

