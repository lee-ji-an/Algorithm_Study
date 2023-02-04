## Info

[11048 이동하기](https://www.acmicpc.net/problem/11048)

<br>

## 💡 풀이 방법 요약

> candy[i][j] = map[i][j] + max(candy[i-1][j], candy[i][j-1], candy[i-1][j-1])
> 
* map에 사탕 개수 저장하고 dist를 -1로 초기화한다.
* top-down과 재귀로 구한다.

### candy(...)
1. (0, 0)이면 map[0][0] 반환
2. dist가 -1이면 점화식 사용해서 사탕 수 구하기
3. 구한 사탕 수 dist에 저장하기

<br>

## 🙂 느낀 점
1. 대각선으로 한 번에 가는 것 보다 옆 또는 아래를 들르는 것이 사탕을 더 많이 가져갈 수 있기 때문에 점화식은 사실상 아래와 같다. 
    ```
   candy[i][j] = map[i][j] + max(candy[i-1][j], candy[i][j-1])
   ```
2. dp 바보인 나는 그래프 문제 풀던 습관으로 dfs 탐색하듯이 풀었고 냅다 했다가 시간초과나서 memoization 도입하는 과정을 거쳤는데 1등님 풀이를 보니 그냥 깔끔하게 입력 받으면서 bottom-up으로 풀더라 .. 다음부턴 웬만하면 그렇게 먼저 생각해봐야겠다.