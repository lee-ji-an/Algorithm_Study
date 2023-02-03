## Info

[12906 새로운 하노이 탑](https://www.acmicpc.net/problem/12906)

<br>

## 💡 풀이 방법 요약

> bfs로 다른 원판이 포함된 막대에서 가능한 경우를 모두 옮겨보기

* towers에 각 막대에 놓여져 있는 원판 문자열 저장
* wrong에 각 막대에 놓여져 있는 다른 원판 개수 저장

### bfs
1. visited:Set<MyStringArray> 로 방문 여부 판별
2. 모든 막대의 wrong이 0이면 횟수 반환
3. i 막대에 원판이 있는 경우 i->j 원판 이동하기
   1. target은 i 막대의 마지막 원판
   2. i 막대에서 target 제거, j 막대에 target 추가
   3. 방문한 적 있으면 패스
   4. target에 따라 wrong[i]와 wrong[j] 조정

### MyStringArray
* Set에 넣을 수 있는 문자열 배열 정의

<br>

## 🙂 느낀 점
처음에는 정말 단순하고 멍청한 방법으로 [A, B, C]를 A/B/C로 변환해서 Set에 저장했는데 너무 오래 걸려서 MyStringArray를 정의해서 사용했고, 실행시간 반 이상 단축됐다 ^^