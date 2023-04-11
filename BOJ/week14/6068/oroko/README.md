## Info
[6068 시간 관리하기](https://www.acmicpc.net/problem/6068)

## 💡 풀이 방법 요약
> 끝나는 시간 기준으로 정렬한 후 일어나기 전에 끝나야 하면 더 일찍 일어나기

1. {시작 시간, 끝나는 시간} 으로 저장
2. 늦게 끝나는 순으로 정렬
3. 일어나는 시간은 최대로 초기화
4. 각 작업에 대해
   1. 일어나는 시간보다 빨리 끝나야 하면 시작 시간에 일어나기
   2. 일어나고 나서 (= 지금 하고 있는 일 끝나고 해야 하면) 해당 작업 시간만큼 더 빨리 일어나기
   3. 일어나야 되는 시간이 음수가 되면 -1 출력하고 끝내기

## 🙂 마무리
