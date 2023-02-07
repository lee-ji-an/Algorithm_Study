## Info
[10942 팰린드롬?](https://www.acmicpc.net/problem/10942)

## 💡 풀이 방법 요약
이웃한 2개의 숫자끼리 검사하여 palindrome인지 여부를 dp에 저장
(i ~ j 인덱스가 palindrome 이면 dp[i][j] = True / 아니면 dp[i][j] = False)
숫자 1개에서 시작(숫자 1개일 때는 무조건 palindrome) -> 왼쪽, 오른쪽으로 하나씩 늘려가며 같은지 검사 -> palindrome 인지 여부 저장
이웃한 숫자 2개에서 시작 -> 왼쪽, 오른쪽으로 하나씩 늘려가며 같은지 검사 -> palindrome 인지 여부 저장

i, j 가 입력으로 들어오면 dp[i][j] 를 반환

## 🙂 마무리
