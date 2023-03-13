## Info
[2668 숫자 고르기](https://www.acmicpc.net/problem/2668)

## 💡 풀이 방법 요약
> DFS
- 결국 모든 사이클을 찾는 문제 -> 그래프 개념 도입
- 단방향 그래프를 만들고, 각 정점에서 모든 정점으로 도달 가능한지 여부를 DFS를 통해 구함
- 서로 다른 두 정점에 대해 양방향으로 모두 도달 가능하다면 두 정점은 사이클의 일부, 즉 `res`에 추가
- 한 정점에 대해서 자기 자신으로의 간선이 있다면 무조건 사이클의 일부, `res`에 추가
- 이렇게 하여 구한 `res` 배열에 중복을 제거 및 정렬하여 출력

## 🙂 마무리
X