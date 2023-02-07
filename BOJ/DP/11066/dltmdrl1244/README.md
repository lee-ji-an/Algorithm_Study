## Info
[11066 파일 합치기](https://www.acmicpc.net/problem/11066)

## 💡 풀이 방법 요약
> 파일의 범위를 나누어서 그 범위 내의 파일들을 하나로 합치는 데 드는 최소 비용을 저장
- index `i`부터 `k` 까지를 하나로 모은 파일과 index `k+1`부터 `j`까지를 하나로 모은 파일을 합치려고 할 때 드는 최소 비용은 `index i~k를 하나로 합치는 데 드는 최소비용` + `index k+1~j를 하나로 합치는 데 드는 최소비용` + `i ~ k 파일들의 합`
- 구간의 길이를 1씩 늘려가면서 마지막에 처음부터 끝까지의 최소 비용을 저장

## 🙂 마무리
라고 제출하면 시간 초과가 뜬다. `N^3`의 시간 복잡도가 생기기 때문인데 이를 `knuth's optimization` 으로 `N^2`로 개선할 수 있다고 한다.
아래는 `knuth's optimization`을 적용하여 python3에서 통과하는 코드인데 아직 이해하지 못했음...
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    knuth = [[0] * n for _ in range(n)]
    s = [0] * n

    for i in range(n):
        s[i] = s[i-1] + arr[i]
        knuth[i][i] = i

    s.insert(0, 0)

    for j in range(1, n):
        for i in range(n-j):
            p = i+j
            dp[i][i+j] = float('inf')

            for k in range(knuth[i][i+j-1], knuth[i+1][i+j] + 1):
                if k < n-1 and dp[i][i+j] > dp[i][k] + dp[k+1][i+j] + s[i+j+1] - s[i]:
                    dp[i][i+j] = dp[i][k] + dp[k+1][i+j] + s[i+j+1] - s[i]
                    knuth[i][i+j] = k

    print(dp[0][n-1])
```
이런게 있다... 하고 당장은 넘어가야 할 듯. dp도 그 자체로 효과적인 문제 해결법이지만 더더욱 개선할 여지가 많구나