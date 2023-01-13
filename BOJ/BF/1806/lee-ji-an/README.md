# 문제 링크
[링크](https://www.acmicpc.net/problem/1806)
# 풀이 방법 요약
1. start, end (two pointer)에 0을 저장, total에는 start~end까지의 합을 저장
2. total이 S보다 크거나 같으면  
   1. start 포인터를 total이 S보다 작을 때까지 오른쪽으로 옮김
   2. minlength를 갱신
3. total이 S보다 작으면  
   end를 한 칸 뒤로 옮김  
   -> 이때 end가 마지막 idx 범위를 넘어가면 종료

# 느낀 점
X