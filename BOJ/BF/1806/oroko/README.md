## Info

[1806 부분합](https://www.acmicpc.net/problem/1806)

<br>

## 💡 풀이 방법 요약

> 각 방향별로 dfs로 5회 밀어서 만들 수 있는 최댓값 구하기

예시) 오른쪽으로 민 경우

| 입력  | 5   | 1   | 3   | 5   | 10  | 7   | 4   |
|-----|-----|-----|-----|-----|-----|-----|-----|
| sum | 5   | 6   | 9   | 14  | 15  | 17  | 21  |
| len | -   | -   | -   | -   | 2   | 2   | 3   |

1. 큐에 각 원소들을 넣고 sum에 큐 내의 원소들의 합을 저장한다.
2. 각 원소들을 하나씩 입력받으면서
   1. 큐에 넣기
   2. sum에 더하기
   3. sum이 M보다 크면 크거나 같은 범위 내에서 최대로 꺼낼 수 있을 만큼 q에서 꺼내고 그만큼 sum에서 빼기
   4. sum이 M과 같거나 큰 경우 중 len을 q.size()의 최솟값으로 갱신하기


<br>

## 🙂 느낀 점
1. 입력 배열 저장 + 부분합 길이별로 탐색 + 큐 사용 -> 메모리 초과
2. 입력 배열 저장 + 부분합 길이별로 탐색 + 큐 대신 인덱스만 저장 -> 시간 초과
3. sum은 long 사용 주의