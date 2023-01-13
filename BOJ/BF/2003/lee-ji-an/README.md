# 문제 링크
[링크](https://www.acmicpc.net/problem/2003)
# 풀이 방법 요약
1. total 에 첫 번째 인덱스 값을 넣음
2. start, end (포인터 역할)에 0을 넣음
3. total < M 일 때 start를 한 칸 오른쪽으로  
   total > M 일 때 end를 한 칸 오른쪽으로  
   total == M 일 때 start 와 end를 둘 다 옮김 , count 1 증가

# 느낀 점
'연속적' 이라는 조건을 이용해서 two pointer로 풀면 시간을 대폭 줄일 수 있음