## Info
[6603 로또](https://www.acmicpc.net/problem/6603)

## 💡 풀이 방법 요약
1. 재귀  
```dfs(start, depth)```  
depth의 의미 : depth 에 들어갈 숫자를 고르겠다  
start의 의미 : 입력받은 숫자 리스트에서 start 인덱스 값 다음부터 넣으세요 (오름차순으로 배열해야하니까)  

depth 가 6이 되면 함수 종료

```Python
for i in range(start, k):
    combi[depth] = s[i]
    dfs(i + 1, depth + 1) 
```
depth칸에 s[i] 를 저장
depth 칸에는 i번째를 넣었으니 depth + 1 칸에는 i + 1번째부터 넣을 수 있겠죠?? -> ```dfs(i + 1, depth + 1)``` 호출

2. combinations 사용  
combinations 쓰는 건 간단하니 설명 생략


## 🙂 마무리
이 문제 옛날에 풀었을 때는 처음에 지이이ㅣ인짜 1도 이해 안 됐는데 잘 이해해놓은 덕분에 이번에는 쉽게 풀었다 ~