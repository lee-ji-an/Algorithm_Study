## Info
[1507 - 궁금한 민호](https://www.acmicpc.net/problem/1507)

## 💡 풀이 방법 요약
1. 입력값에서 edge의 weight가 작은 것부터 차례대로 본다.
2. 내가 현재까지 만든 grpah의 sp 리스트를 sp_list에 저장
3. 현재 edge의 weight와 sp_list의 값이 같으면 넘어감
4. 현재 존재하는 경로에서 현재 edge를 거쳤을 때 distance를 업데이트
- 정답 거리 리스트와 같을 때만 저장
- 정답 거리 리스트보다 작다면 만들 수 없는 거리 조합이므로 -1 print


## 🙂 마무리