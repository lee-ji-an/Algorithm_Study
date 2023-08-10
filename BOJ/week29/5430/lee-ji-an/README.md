## Info
[5430 AC](https://www.acmicpc.net/problem/5430)

## 💡 풀이 방법 요약
> two pointer

1. `R`
앞, 뒤를 나타내는 ptr 변수를 하나 놓고 R 이 나올 때마다 ptr의 값을 바꿈. T->F, F->T

2. `D`
ptr 값에 따라서 deque에 있는 값을 pop or popleft 함.
- ptr == T : popleft
- ptr == F : pop

## 🙂 마무리

