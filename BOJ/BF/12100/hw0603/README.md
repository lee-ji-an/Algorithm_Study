## Info
[12100 2048 (Easy)](https://www.acmicpc.net/problem/12100)

## 💡 풀이 방법 요약
[13460 구슬 탈출 2](https://www.acmicpc.net/problem/13460) 와 비슷한 방식으로 풀이한다.  
전체적인 구조는 `itertools.product`를 순회하는 메인 반복분 안에서 모든 경우를 BF를 통해 확인하고, 반복 시 마다 최댓값을 업데이트하는 구조이다. 
```
result = 0
for dirlist in product(("상", "하", "좌", "우"), repeat=5):
    board = [row[:] for row in orig_board]
    for dir in dirlist:
        move(dir)
    result = max(max(max(x) for x in board), result)
```
2048 게임의 규칙에 맞게 `move(dir)` 함수를 정의해 주어야 하는데, 전달받은 `dir` 값에 따라 `board` 배열을 순회하며 방향에 맞게 현재 조사하고 있는 줄에 대하여 알맞은 값을 `line`에 추가해 주면 된다.  
`line`은 이동 방향에 따라 새로운 데이터를 추가해야 하는 방향이 달라지므로, 자료구조로 `deque`를 사용한다. 
   
각 칸을 순서에 맞게 순회하며 그 값이 `0`이라면 skip하고, `0`이 아닌 경우에는 같은 숫자가 연속으로 등장했을 때 합쳐지는 기능을 구현하기 위해 버퍼로 사용할 변수 하나를 두어 활용한다.  
`0`이 아닌 숫자는 우선적으로 버퍼에만 저장해 두었다가 다음에 등장하는 `0`이 아닌 숫자가 현재 버퍼와
1. 같다면 `현재 버퍼의 값 << 1` 을 `line`에 추가하고 버퍼를 비운다.
2. 다르다면 현재 버퍼의 값을 `line`에 추가하고 버퍼에 현재 조사하는 값을 저장한다.
반복문 종료 후 버퍼에 값이 저장되어 있다면 `line`에 추가해 주고, 저장된 `line`의 길이와 `N`값을 비교하여 부족한 길이만큼 `0`을 삽입해 준다.  
  
위와 같은 과정을 거치면 `line`에 현재 조사중인 줄의 이동 완료 후 데이터가 저장될 것이다. 이동방향을 고려하여 원본 배열의 해당 줄을 `line`으로 대체해 주면 된다.

## 🙂 마무리
앞, 뒤에서 모두 삽입/삭제 연산이 일어날 경우 `deque`의 사용을 고려하자.  
단순한 구조의 2차원 배열을 깊은 복사해야 하는 경우 `copy.deepcopy()` 보다 `[row[:] for row in 2DList]` 가 훨씬 빠르다. (상세 동작에는 물론 차이가 있음)  
  
자세한 설명은 아래 링크 참조  
[Is python deepcopy more efficient... Stackoverflow](https://stackoverflow.com/questions/20772885/is-python-deepcopy-more-efficient-than-custom-code-or-less-efficient-predictabl)  
[[Python] 파이썬 리스트 복사](https://codesyun.tistory.com/198)
