## Info

[16235 나무 재테크](https://www.acmicpc.net/problem/16235)

<br>

## 💡 풀이 방법 요약
> 계절 순서대로 구현
- 봄과 여름을 합쳐서 각 나무별로 양분을 먹고(봄), 못 먹으면 `dead`에 저장했다가 더해줌(여름)
- 가을 겨울을 합쳐서 크기가 5배수인 나무 주위에 크기 1짜리 나무 생성하고 비료 뿌림

<br>

## 🙂 느낀 점
구현이 어렵지는 않았는데 적절한 자료구조를 사용하지 않으면 시간 초과가 발생했다.
나무들의 정보를 리스트로 받았는데 `deque`로 하니까 시간이 줄어들었다.
또한 같은 칸의 나무들에 대해 크기순으로 정렬하지 않아도 `deque` 자료구조의 `append`와 `appendleft` 로 충분히
크기순으로 정렬할 수 있다는 것을 알았다.