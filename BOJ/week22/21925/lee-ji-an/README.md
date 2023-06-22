## Info
[21925 짝수 팰린드롬](https://www.acmicpc.net/problem/21925)

## 💡 풀이 방법 요약
#### 1. dp  
    (1) 2차원 리스트에 i ~ j 가 팰린드롬인지 판단한 T/F를 저장
    (2) dp[idx] : idx 까지 짝수 팰린드롬의 최대 갯수  
                  i ~ idx 로 끝나는 팰린드롬이 있으면 dp[i - 1] + 1 를 저장

#### 2. greedy
    길이가 N인 수열 A를 탐색
    (1) stack이 비었거나 stack[top]과 같으면 -> stack에 push
    (2) stack[top]과 현재 수열의 값이 같으면
        - 팰린드롬인지 확인 (check 함수)
        - T -> 정답 횟수를 증가시키고 idx를 팰린드롬 마지막 인덱스 뒤로 이동시킴
        - F -> stack에 push

## 🙂 마무리
