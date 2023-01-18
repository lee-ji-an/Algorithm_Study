## Info

[12886 돌 그룹](https://www.acmicpc.net/problem/12886)

<br>

## 💡 풀이 방법 요약

> bfs로 세 숫자가 같아질 때까지 탐색하기

### Play
1. stone[] : 각 돌 그룹의 돌 개수
2. 생성자 : 항상 오름차순으로 저장
3. success() : 모든 그룹의 돌 개수가 같은지 확인
4. equals(), hashCode() : Play를 Collections의 제네릭 타입으로 사용하기 위해 오버라이딩

### bfs
1. q에 넣어서 탐색
2. visited 대신 set을 사용해서 무한루프 방지
3. 성공하면 1 반환, 큐가 끝나도 성공못하면 0 반환

<br>

## 🙂 느낀 점
equals와 hashCode 기억해보자