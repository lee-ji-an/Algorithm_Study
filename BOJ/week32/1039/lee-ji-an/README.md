## Info
[1039 교환](https://www.acmicpc.net/problem/1039)

## 💡 풀이 방법 요약
> BFS
1. k 번 만큼 반복문을 돌면서 bfs 수행
2. 바꿀 숫자 자리 2개를 조합으로 선택
3. visited는 set으로 관리, 선택한 2자리를 바꾸고 visited에 없으면 다시 q에 넣고, visited에도 추가

## 🙂 마무리
BFS로 시간초과가 날 줄 알았는데 안 났다. 그 이유는 뭘까