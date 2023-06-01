## Info
[4256 트리](https://www.acmicpc.net/problem/4256)

## 💡 풀이 방법 요약
> D&C

1. preorder에서 루트 번호를 찾고, 그 번호를 inorder에서 찾기
2. inorder에서 루트를 기준으로 왼쪽 인덱스에 있는 것은 왼쪽 서브트리, 오른쪽은 오른쪽 서브트리
3. D&C로 왼쪽-오른쪽-루트 순으로 탐색해서 출력

## 🙂 마무리
