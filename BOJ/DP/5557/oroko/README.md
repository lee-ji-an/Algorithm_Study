## Info
[5557 1학년](https://www.acmicpc.net/problem/5557)

## 💡 풀이 방법 요약
> dp[i][j] += dp[i-1][j], i번째까지 봤을 때 j가 되는 경우의 수

* temp에 다음에 탐색할 수 목록을 넣고 set으로 옮겨서 set으로 탐색한다.
* set과 dp에 첫번째 수를 넣어놓고 시작한다.
* dp 내에 들어갈 수는 long

## 🙂 느낀 점
혼자서 푼 것이 대견한 내 자신 ㅠㅠ