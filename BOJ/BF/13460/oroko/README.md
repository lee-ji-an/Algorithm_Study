## Info

[13460 구슬 탈출 2](https://www.acmicpc.net/problem/13460)

<br>

## 💡 풀이 방법 요약

> bfs로 빨간 구슬이 구멍에 빠질 때까지 이동할 수 있으면 이동하기 

1. map:boolean[]에 갈 수 있는지(장애물 없는지) 여부 표시
2. bfs로 동서남북 방향으로 10회 이하까지 탐색하기

### Pos 클래스
* 빨간 구슬과 파란 구슬의 위치, 시도 횟수 저장
* pq에서 시도 횟수로 정렬할 수 있도록 설정
* pq에 다음 원소 저장할 때 사용하기 위해 clone 추가, clone했으면 시도 횟수 증가
* move 함수
  * 빨간 구슬과 파란 구슬이 구멍에 안빠졌는지, 이동할 위치에 장애물이 없는지 확인 후 이동
  * 둘 중 하나가 안움직였는데 나머지가 움직여서 둘이 겹쳐졌으면 움직인 것 원위치 시키기

### bfs()
* pq 이용해서 시도 횟수 작은 경우부터 탐색하기
* 파란 구슬 빠진 경우 배제(빨간 구슬도 빠졌어도 안됨)
* 파란 구슬 안빠지고 빨간 구슬 빠졌으면 성공
* 10회 시도했는데도 안됐으면 배제
* 동서남북에 대해서 구슬 두 개 가능한 만큼 이동시켜서 pq에 넣기

### 객체 깊은 복사
내가 만든 객체를 깊은 복사 할 때는 Cloneable 인터페이스의 clone 함수를 구현하면 된다.
```java
@Override
public MyObject clone() {
    try {
        MyObject clone = (MyObject) super.clone();
        // TODO: copy mutable state here, so the clone can't change the internals of the original
        return clone;
    } catch (CloneNotSupportedException e) {
        throw new AssertionError();
    }
}
```

<br>

## 🙂 느낀 점
처음으로 골드1 문제를 풀었다 !! <br>
bfs 할 때 당연히 visited를 설정했고, 처음에 빨간 구슬 방문했는지만 표시했는데 안되길래 두 구슬 다 표시했는데도 안됐다.
그냥 방문했는지 여부를 고려안해야 했다. 그럴 것 같은 느낌이 들었지만 visited를 쉽게 포기할 수는 없었다. visited 안써야 되는 bfs 문제 처음 본 것 같다 ...