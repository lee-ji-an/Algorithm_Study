## Info
- [2637 장난감 조립](https://www.acmicpc.net/problem/2637)

## 💡 풀이 방법 요약
> Topological Sort
1. Topological Sort를 이용해서 부품끼리의 의존성을 고려해 순서를 정함.
   - 예를들어, 2 번 부품을 만들 때 4번 부품이 사용된다면 / 2번이 4번보다 먼저 와야 함.
   - 2번 부품을 4번부품 + ... + ... 로 바꾸고 그 다음에 4번 부품을 바꿔야 한 번에 바꿀 수 있음.
2. Topological Sort 순서대로 탐색하면서 완제품의 부품을 변환함.

## 🙂 마무리
Topological Sort를 사용하는 참신한 문제였다.