## Info
[148652 유사 칸토어 비트열](https://school.programmers.co.kr/learn/courses/30/lessons/148652)

## 💡 풀이 방법 요약
`a : pos의 몫 / b : pos의 나머지`

1. a 번째 수까지는 1을 모두 카운트 하면 됨 -> 4의 지수승 만큼 계산  
    b는 남은 숫자 갯수 -> 다시 재귀 호출 
2. a <= 1 :  
    -> `4 ** (n_level - 1) * a + dfs(n_level - 1, b)`
3. a == 2 : b를 무시해도 됨 -> 어차피 남은 b의 갯수는 모두 0이기 때문   
    -> `4 ** (n_level - 1) * a`
4. a > 2 : 0이 한 개 속해있으므로 a-1 개 만큼 카운트   
    -> `4 ** (n_level - 1) * (a - 1) + dfs(n_level - 1, b)`

## 🙂 마무리

