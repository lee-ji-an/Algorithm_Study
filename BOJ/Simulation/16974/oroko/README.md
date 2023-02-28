## Info

[16974 레벨 햄버거](https://www.acmicpc.net/problem/16974)

<br>

## 💡 풀이 방법 요약
> dp로 각 레벨별 패티 수 구하고 분할 정복으로 먹은 패티 수 구하기

1. dp로 각 레벨별 패티 수를 구한다. (patty[i] = 1 + patty[i-1] * 2)
2. 분할 정복으로 먹은 패티수를 구한다.

### burger(...)
* level이 0이면 patty[level] 반환
* X가 left이면 빵이므로 0 반환
* X가 right이면 해당 레벨을 다 먹었으므로 patty[level] 반환
* X가 mid이면 왼쪽 patty[level-1] 수에 해당 레벨에서 새로 추가된 패티 한장까지 먹었으므로 patty[level-1]+1
* X가 mid보다 왼쪽이면 왼쪽 level-1에서 먹은 수
* X가 mid보다 오른쪽이면 mid까지 먹은 수 + 오른쪽 먹은 수

<br>

## 🙂 느낀 점
처음에는 그냥 dp로 문자 더하고 boolean 더하고 다 해봤는데 숫자가 너무 커서 heap 메모리를 초과했다는 에러를 봤다 ...<br>
엄청 큰 수를 탐색해야 할 때는 **분할정복**을 떠올려보자!