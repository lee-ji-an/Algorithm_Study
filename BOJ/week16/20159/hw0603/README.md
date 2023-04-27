## Info
[20159 동작 그만. 밑장 빼기냐?](https://www.acmicpc.net/problem/20159)

## 💡 풀이 방법 요약
'밑장을 뺄 수 있는 횟수가 최대 1번' 이라는 것이 조건이므로, 밑장빼기를 아예 안 해도 되고, 상대방에게 밑장을 줘도 되고, 내가 밑장을 가져도 된다.  
1. 밑장을 빼지 않는 경우
   - 그냥 누적합으로 구한다.
2. 내가 밑장을 가지는 경우
   - 밑장빼기를 한 시점을 포함해서 상대가 가졌어야 할 카드들과 내가 가졌어야 할 카드가 바뀐다.
3. 상대방에게 밑장을 주는 경우
   - 그 시점 이후부터 내가 가졌어야 할 카드와 상대방이 가졌어야 할 카드가 바뀐다.

(1)의 경우 정훈이의 점수를 `origSum`에 저장해 두고, (2), (3)을 시뮬레이션하면서 뒤에서부터 거꾸로 '이 시점에서 밑장빼기를 했다면 합은 어떻게 될까?'의 느낌으로 접근하여 최댓값을 구한다.


## 🙂 마무리
문제 보자마자 누적합 문제인 것 같아서 `itertools`를 적극 활용해서 풀어 봤다.  
원본 코드는 아래에 첨부.
```python
from itertools import accumulate
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 밑장 빼기 한 번도 안 했을 때
origSum = tuple(accumulate(card for idx, card in enumerate(arr) if not (idx % 2)))[-1]
ans = origSum

# 정훈이 차례에 밑장 빼기 했을 때
score = origSum
for i in range(N-1, 0, -2):
    score += (arr[i] - arr[i-1])
    ans = max(ans, score)

# 상대 차례에 밑장 빼기 했을 때
score = origSum
for i in range(N-2, 1, -2):
    score -= (arr[i] - arr[i-1])
    ans = max(ans, score)

print(ans)
```

