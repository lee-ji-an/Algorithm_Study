## Info
- [1655 가운데를 말해요](https://www.acmicpc.net/problem/1655)

## 💡 풀이 방법 요약
> heap

1. left_heap, right_heap을 선언
   - left_heap : 중간보다 작은 숫자를 저장 / max heap으로 관리
   - right_heap : 중간보다 큰 숫자를 저장 / min heap으로 관리
2. 순서대로 숫자를 탐색해서 left_heap 또는 right_heap에 넣고 left_heap의 root 노드에 항상 가운데 숫자를 유지 
    ```
   숫자가 홀수 개일 때 
   ex) 1 2 5 5 7
      - left_heap : 1 2 5
      - right_heap : 5 7
   
   숫자가 짝수 개일 때 
   ex) -99 2 5 5 7 10
      - left_heap : -99 2 5
      - right_heap : 5 7 10
   ```
    


## 🙂 마무리
