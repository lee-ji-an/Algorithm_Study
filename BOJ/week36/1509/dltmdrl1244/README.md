## Info
- [1509 팰린드롬 분할](https://www.acmicpc.net/problem/1509)

## 💡 풀이 방법 요약
> dp[i] = i번째 문자까지의 팰린드롬 분할 개수의 최솟값

- i번째 등장한 알파벳을 A라고 하자
- i가 한 글자 이상의 팰린드롬에 포함되기 위해서는 i번째 이전에 A가 나왔어야 한다.
- 이것을 빠르게 찾기 위해서 미리 각 알파벳이 등장하는 위치를 딕셔너리에 저장한다.
- i번째 이전에 j번째에 A가 나왔었다고 하면 j부터 i까지가 팰린드롬인지를 판별한다.
- 만약 팰린드롬이라면 j 이전까지의 dp 값에다가 j~i까지의 팰린드롬 1개로 만들 수 있다.
- 이것을 i 전까지 반복한다.
- 각 iteration 마다 (이전에 나온 문자 개수) * n이 소요

## 🙂 마무리
오랜만에 디피라서 정신을 못 차렸다
각 iteration마다 n만에 수행이 불가해서 worst case로 충분히 시간 초과가 날 수 있을 것 같은데 다행히(?) 통과했다.
더 나은 방법이 생각이 나질 않았음..

아래는 처음에 생각했었던 2차원 DP 풀이 (시간초과 남)
```
python
import sys
input = sys.stdin.readline


def isPalin(arr):
    return arr == arr[::-1]

arr = input().rstrip()
n = len(arr)
dp = [[n for _ in range(n)] for _ in range(n)]

# 0 ~ 34

for i in range(n):
    for j in range(i, n):
        dp[i][j] = j - i + 1

# l이 n-1까지 i는 0부터 2까지
for l in range(2, n+1):
    for i in range(n-l+1):
        if isPalin(arr[i:i+l]):
            dp[i][i+l-1] = 1

        else:
            for j in range(i, i+l-1):
                dp[i][i+l-1] = min(dp[i][i+l-1], dp[i][j] + dp[j+1][i+l-1])

print(dp[0][n-1])
```