## Info
[15989 1, 2, 3 더하기 4](https://www.acmicpc.net/problem/15989)

## 💡 풀이 방법 요약
`dp[i] = 1, 2, 3만으로 i를 만들 수 있는 경우의 수`로 정의하고, 1, 2, 3 각각을 통해 만들 수 있는 경우의 수를 누적하면 된다.  
`1`로 어떤 숫자를 만들 수 있는 경우는 한 가지씩 밖에 없으므로, 초기의 dp값은 모두 `1`로 초기화 해 둔다.  
  
```python
for i in (2, 3):
    for j in range(i, 10000+1):
        dp[j] += dp[j-i]
```
에서, 어떤 수 `N`을 `2`만으로 만들 수 있는 경우의 수는 `N-2`를 만들 수 있는 경우의 수와 같다는 사실을 일반화하여 조사 대상 숫자(=2, 3)에 대해 dp배열의 끝까지 루프를 돌며 `dp[N] += dp[N-num]` 을 계산해 준다.


## 🙂 마무리
dp값의 의미는 잘 정의했지만 구현에서 막혀서 다른 풀이를 조금 참고했다.
