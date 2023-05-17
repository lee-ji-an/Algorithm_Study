## Info
[22945 팀 빌딩](https://www.acmicpc.net/problem/22945)

## 💡 풀이 방법 요약
> 쓰리포인터(?)

1. min_ptr : 팀 빌딩에서 능력치의 최솟값을 가리키는 ptr
    - min_ptr 은 능력치의 크기 순으로 정렬한 후 크기 순으로 탐색
2. right_ptr : 맨 오른쪽 부터 시작해서 min_ptr이 가리키고 있는 값보다 클 때까지 왼쪽으로 이동하는 ptr
3. left_ptr : 맨 왼쪽 부터 시작해서 min_ptr이 가리키고 있는 값보다 클 때까지 오른쪽으로 이동하는 ptr
   - min_ptr이 능력치의 최솟값이므로 right_ptr, left_ptr은 무조건 min_ptr이 가리키는 값보다 크거나 같아야 함
   - 따라서 맨 왼쪽 (left_ptr), 맨 오른쪽 (right_ptr)에서 시작해서 min_ptr보다 큰 수가 나올 때까지 범위를 좁힘
4. left_ptr ~ min_ptr / min_ptr ~ right_ptr 거리가 더 긴 것을 비교해서 정답을 갱신

## 🙂 마무리
 크기와, idx 거리를 이용해야 하는 문제라서 신선했다.
 