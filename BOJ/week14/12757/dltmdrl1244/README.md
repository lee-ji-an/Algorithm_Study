## Info
[12757 전설의 JBNU](https://www.acmicpc.net/problem/12757)

## 💡 풀이 방법 요약
> Red-Black binary search tree 사용
- Red black binary search tree란 기존 이진 탐색 트리를 개선하여 항상 트리의 깊이를 logN으로 제한할 수 있는 방법임
- 2-3 트리를 구성하되 간선의 종류를 Red, Black (내부 연결, 외부 연결)으로 나누어 한 노드에 키가 3개가 되면 가운데 키를 부모로 올리는 split 작업을 거침
- floor, ceiling 함수의 경우 해당 key보다 작지 않은/크지 않은 가장 작은/큰 key를 리턴함

## 🙂 마무리
알고2 시간에 배운 red black tree 구현 코드를 조금 수정하여 거의 그대로 사용했음...
