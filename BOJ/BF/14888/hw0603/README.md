## Info
[14888 연산자 끼워넣기](https://www.acmicpc.net/problem/14888)

## 💡 풀이 방법 요약
백트래킹, 재귀 없이 그냥 브루트포스로 풀이했다.  
`opt_list`에 사용할 수 있는 연산자들의 문자를 저장해 두고, `itertools.permutations`를 활용하여 모든 경우를 순회한다. 이때, 중복되는 경우가 나올 수 있으므로 `set()`으로 중복 제거를 해 준다.  
계산할 때는 `eval()`을 활용하여 식을 계산해 준다.

## 🙂 느낀 점
저번에 비슷한 문제 풀었을 때는 `eval()`로 시간 초과가 났었는데 드디어 `eval()` 써서 풀었다!
