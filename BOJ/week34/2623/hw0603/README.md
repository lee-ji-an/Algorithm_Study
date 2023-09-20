## Info
[2623 음악프로그램](https://www.acmicpc.net/problem/2623)

## 💡 풀이 방법 요약
[1766 문제집](https://www.acmicpc.net/problem/1766)이나, [2252 줄 세우기](https://www.acmicpc.net/problem/2252)와 유사한 위상정렬 문제이다.
  
큐를 하나 선언하고, 해당 큐는 의존성 없이 바로 줄 세울 수 있는 가수들의 대기열로 정의한다. 따라서 큐의 초깃값은 초기 진입차수가 0인 모든 가수들이다.  
  
다음으로, 큐에서 한 가수씩 `pop()` 하며,  
1. 줄을 세우고
2. 방금 줄 세운 가수 때문에 의존성 걸려 있던 가수들의 진입차수를 모두 `1` 감소시킨다.
3. 만약 감소 후 진입차수가 `0`이 된 가수이 있다면 큐에 삽입한다.
4. 위 과정을 큐가 빌 때 까지 반본한다.

`1766 문제집` 에서는 문제들 간의 우선순위 뿐만 아니라 문제 번호에 따른 기본 우선순위가 존재하였기 때문에 큐가 아닌 우선순위 큐(heapq)를 사용했었지만, 이 문제에서는 별다른 추가 조건이 없으므로 일반 큐를 사용하거나 우선순위 큐를 사용해도 되고, 랜덤하게 골라도 된다.(스페셜 저지 문제)

## 🙂 마무리
위에서 언급한 두 문제와 달리 예외처리를 좀 해줘야 한다.  
내가 처음 틀렸던 부분은 여러 PD가 같은 종속성 튜플을 제출했을 경우, 진입차수가 중복으로 올라가게 되어 종속성 해제가 제대로 안 되는 문제를 놓치고 있었다.
순회 전 `depTupleList`를 `set`으로 변환해 주어 중복 제거를 통해 해결했다.