## Info

[1644 소수의 연속합](https://www.acmicpc.net/problem/1644)

<br>

## 💡 풀이 방법 요약

> [2003 수들의 합 2](https://www.acmicpc.net/problem/2003) 문제에서 입력 배열을 소수 수열로 바꾸면 된다.

1. 1부터 N까지 탐색하면서 소수인지 확인한다.
2. 소수이면
   1. 큐에 넣기
   2. sum에 더하기
   3. sum이 M보다 크면 작거나 같아질 때까지 q에서 꺼내고 그만큼 sum에서 빼기
   4. sum이 M과 같아지면 cnt 증가시키기

<br>

## 🙂 느낀 점
소수 구하는 함수는 자동으로 나오기