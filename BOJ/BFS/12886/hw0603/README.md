## Info
[12886 돌 그룹](https://www.acmicpc.net/problem/12886)

## 💡 풀이 방법 요약
생각하기 쉽게 각 돌 그룹이 항상 `A > B > C`를 만족하도록 유지한다.  
먼저 입력받은 값 3개를 정렬한 튜플을 큐에 삽입하고, 문제의 조건에 맞게 큐에서 원소를 꺼낼 때 마다 새로운 `(A, B, C)`튜플을 만들어 큐에 삽입하며 BFS를 진행한다.  
방문 체크를 위해서는 튜플을 원소로 갖는 `set`을 사용했다.

## 🙂 마무리
알고리즘 분류가 BFS인 것을 미리 알고 있어서 쉽게 풀었는데, 모르고 풀었다면 생각보다 어려웠을 것 같기도..?
