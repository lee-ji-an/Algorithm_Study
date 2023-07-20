## Info
[2110 공유기 설치](https://www.acmicpc.net/problem/2110)

## 💡 풀이 방법 요약
> binary search 사용
1. start = 1, end = max - min 으로 초기값 세팅
2. mid 를 기준으로 했을 때 설치 가능한 집이 몇 개 나오는지 검사
3. C 보다 크거나 같으면 간격을 더 넓혀도 됨 -> start = mid + 1  
C 보다 작으면 간격을 더 좁혀야 함 -> end = mid - 1

## 🙂 마무리
binary search를 이렇게 사용해본 건 처음이라서 새로웠다.