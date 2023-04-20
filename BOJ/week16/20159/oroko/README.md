## Info
[20159 동작 그만. 밑장 빼기냐?](https://www.acmicpc.net/problem/20159)

## 💡 풀이 방법 요약
> 누적합

각 턴에 밑장을 빼면 그 뒤부터 퐁당퐁당의 누적합으로 카드의 합이 정해진다 !

1. 누적합 구하기
   * ex) `cards[6] : cards[0] + cards[2] + ... + cards[6]`
   * ex) `cards[7] : cards[1] + cards[3] + ... + cards[7]`
2. i번째 턴에 밑장 뺐을 때 최댓값 구해서 max 갱신하기
   1. i번째가 내 턴일 경우 : cards[i-2] + (cards[N-1]-cards[i-1])
   2. i번째가 상대일 경우 : cards[i-1] + (cards[N-3]-cards[i-2])

## 🙂 마무리
이 영광을 현준이에게 ^^,,

