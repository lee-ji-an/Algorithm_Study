## Info

[11058 크리보드](https://www.acmicpc.net/problem/11058)

<br>

## 💡 풀이 방법 요약

> 어떤 칸을 버퍼로 사용하여 `Ctrl+V`를 여러 번 하는 것이 가장 효과적인지
- `dp[i]`를 `키보드를 i번 눌러 나타낼 수 있는 문자의 최대 갯수` 로 정의
- `dp[7]`은 다음 값들 중 하나이다
  - `Ctrl+A` `Ctrl+C` `Ctrl+V`에 최소 3번이 소요되므로 3칸 이내로 떨어진 칸은 참조 불가능
  - `dp[4]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V` 를 추가하여 `dp[4] * 2`
  - `dp[3]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V`를 추가하여 `dp[3] * 3`
  - `dp[2]`는 버퍼를 만들 수가 없으므로 (`A` + `Ctrl+A` `Ctrl+C`에 최소 3번 소요) 안 됨
- `dp[11]`은 다음 값들 중 하나이다
  - `dp[8]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V`
  - `dp[7]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V`
  - `dp[6]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V`
  - `dp[5]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V`
  - `dp[4]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V`
  - `dp[3]`에서 `Ctrl+A` `Ctrl+C` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V` `Ctrl+V`
---
자기보다 j칸 떨어진 지점의 `dp[i-j]` 값을 `j-1`번 곱한 값들 중 최댓값이 `dp[i]
<br>

## 🙂 느낀 점
노가다의 산물이다
