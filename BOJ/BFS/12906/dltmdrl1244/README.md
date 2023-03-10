## Info
[12906 새로운 하노이 탑](https://www.acmicpc.net/problem/12906)

## 💡 풀이 방법 요약
> 특정 막대기에 속하지 않아야 하는 원판이 있으면 맨 위 원판을 옮기는 작업을 반복

- 같은 조합을 여러 번 반복 (`A, AA, AA`에서 `A, A, AAA` 갔다가 다시 `A, AA, AA`로 오는)하지 않도록 `set` 에다 기록해 둔다.
- 큐에 삽입할 때 복사하는 과정을 거친다.

## 🙂 마무리
set에 넣을 때 리스트로 넣을 수가 없어서 튜플로 만드는 과정을 거쳤는데 더 나은 방법이 있을 것 같다.

불순한 원판이 있는지 여부를 `in` 연산으로 하기에 시간이 오래 걸릴 것 같아서 전체 막대기에 꽂힌 원판의 비중의 합을 구하는 방식으로 구현하였는데
전체 최대 원판 개수가 10개니까 `in` 탐색에 기껏해야 10번 수행하므로 애초에 크게 부담이 없었던 것 같다.

오히려 합을 구하는 방식이 더 오래 걸림...