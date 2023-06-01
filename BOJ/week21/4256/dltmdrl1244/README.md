## Info
[4256 트리](https://www.acmicpc.net/problem/4256)

## 💡 풀이 방법 요약
> 분할 정복과 재귀를 적절히 믹스
- preorder에서 가장 먼저 나오는 노드가 루트노드이고
- inorder에서는 루트노드가 중간에 있다.
- 루트노드를 inorder에서 찾아서 이 인덱스를 기준으로 왼쪽 sub tree, 오른쪽 sub tree를 정할 수 있다.
- 그리고 postorder이므로 마지막에 root 노드를 출력한다.
- 이를 재귀적으로 반복한다.

## 🙂 마무리
x