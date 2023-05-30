## Info
[2616 소형기관차](https://www.acmicpc.net/problem/2616)

## 💡 풀이 방법 요약
> 누적합, dp 사용

`dp[i][j]` : 1 ~ i 번째 소형 기관차들이 j 까지의 범위에서 태울 수 있는 승객의 최댓값

```Python
dp[i][j] = max(
                dp[i][j - 1], dp[i - 1][j - train_len] + (prefix_sum[j] - prefix_sum[j - train_len])
            )
```
j 번째 객차를 포함하지 않았을 때 : `dp[i][j - 1]`  
j 번째 객차를 포함할 때 : `dp[i - 1][j - train_len] + (prefix_sum[j] - prefix_sum[j - train_len])`

이 두 경우 중에 최댓값을 저장

## 🙂 마무리
dp 라는 생각은 했지만 어떻게 풀어야 할지는 생각해내지 못해서 구글링했다  
1. 0-1 knapsack 유형
2. 파일합치기 유형  
dp 유형이 이렇게 2개로 나뉘는 것 같다.  
이번 문제는 1번 유형
