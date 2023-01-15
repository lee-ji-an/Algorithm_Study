## Info

[1208 부분수열의 합 2](https://www.acmicpc.net/problem/1208)

<br>

## 💡 풀이 방법 요약

> 수열을 반으로 나눠서 각각 부분합 리스트 구하고 투포인터로 합이 S가 되는 경우의 수 세기

| 인덱스         | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|
| 왼쪽 부분합 리스트  | -10 | -7  | -3  | 0   | -   | -   | -   | -   |
| 오른쪽 부분합 리스트 | 13  | 11  | 8   | 6   | 5   | 3   | 0   | -2  |
| i           | 0   | 0   | 0   | 1   | 1   | 2   | 2   | 2   |
| j           | 0   | 1   | 2   | 2   | 3   | 3   | 4   | 5   |
| sum         | 3   | 1   | -2  | 1   | -1  | 3   | 2   | 0   |

1. 0 ~ N/2-1, N/2 ~ N-1 각 범위 내 수열의 부분수열의 합 리스트를 구한다.
2. 각 리스트를 정렬하고, 투포인터로 각 리스트의 원소의 합이 S가 되는 경우의 수를 센다.

<br>

## 🙂 느낀 점
1. 원소가 N개인 수열의 부분수열의 합 구하기 => 실패
2. 중간에서 만나기 + 이중 for문으로 각 리스트의 원소 합 탐색 => 시간초과
3. 중간에서 만나기 + 투포인터로 탐색 => long으로 바꾸고 나서 통과

결국 풀이 끝까지 다봤다 ... 개수가 long !!!