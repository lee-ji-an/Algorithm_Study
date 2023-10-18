## Info
[118667 두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

## 💡 풀이 방법 요약
> Two Pointer

- 두 큐의 합을 m 으로 만들어야 한다면, queue1의 합 -> m이면 queue2의 합은 자동으로 m이 됨.
- 따라서, queue1을 기준으로 연산

1. start_ptr, end_ptr 이 queue1의 첫 원소와 마지막 원소를 가리킴
2. start_ptr ~ end_ptr 사이 수의 합이 m 보다 작으면 end_ptr 을 뒤로 옮김
3. start_ptr ~ end_ptr 사이 수의 합이 m 보다 크면 start_ptr 을 뒤로 옮김
4. 포인터를 한 칸씩 옮길 대마다 answer을 1 증가시킴.
5. m 과 포인터가 가리키고 있는 위치 사이 수의 합이 같아진다면 -> `return answer`
6. 모든 탐색 후에도 같아지는 순간이 없으면 -> `return -1`

## 🙂 마무리

