## Info
- [142085 디펜스 게임](https://school.programmers.co.kr/learn/courses/30/lessons/142085)

## 💡 풀이 방법 요약
> Greedy, heapq

- heapq로 현재 소모한 병사의 수를 max heap으로 관리 (각 라운드마다 소모한 병사의 수를 push)
1. 남은 병사의 수보다 적의 수가 더 클 때
    - 무적권이 남아있다면 -> 현재 적의 수를 먼저 push하고 heapq에서 가장 큰 병사를 소모한 라운드를 pop
    - 무적권이 남아있지 않다면 -> 게임 종료
2. 남은 병사의 수보다 적의 수가 더 작을 때
   - heapq 현재 라운드에 소모할 병사의 수를 push

## 🙂 마무리
