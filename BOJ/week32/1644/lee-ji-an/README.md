## Info
[1644 소수의 연속합](https://www.acmicpc.net/problem/1644)

## 💡 풀이 방법 요약
> Two pointer
1. N 까지의 소수를 모두 찾아 리스트에 저장.
2. N 까지의 소수를 모두 저장한 리스트에서 Two pointer로 start ~ end의 합이 N이 되는 순간을 찾음.
    - start ~ end < N : end 를 뒤로 옮김
    - start ~ end > N : start 를 뒤로 옮김
    - start ~ end = N : cnt 1 증가 / start, end를 뒤로 옮김

## 🙂 마무리
