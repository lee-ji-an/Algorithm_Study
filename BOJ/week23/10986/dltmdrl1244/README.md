## Info
[10986 나머지 합](https://www.acmicpc.net/problem/10986)

## 💡 풀이 방법 요약
> 딕셔너리에다가 나머지 정보를 저장
- 만약 3으로 나누어 떨어지는 구간합을 찾으려고 할 때 누적합을 3으로 나눈 나머지가 1이라면 앞에서 `누적합이 1이였던 횟수` 만큼의 구간합을 3으로 나누어 떨어지게 할 수 있음 (그 구간까지를 잘라내면 된다.)
- 따라서 순차 탐색하면서 누적합을 기록하되 그 수를 m으로 나눈 나머지를 딕셔너리에다가 기록, 다음에 같은 숫자를 만났을 때 앞에서 그 나머지가 몇 번 나왔는지를 구해서 정답에 더해주면 된다.

## 🙂 마무리