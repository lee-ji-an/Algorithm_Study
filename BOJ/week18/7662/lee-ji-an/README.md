## Info
[7662 이중 우선순위 큐](https://www.acmicpc.net/problem/7662)

## 💡 풀이 방법 요약
> max heap, min heap 사용

1. 삽입
- max heap, min heap에 모두 삽입
- 같은 수가 나올 수 있으므로 입력 순서도 함께 heap에 저장, (number, order)

2. 삭제
- pop 한 데이터들을 set 에 저장해서 유효한 데이터인지 검사
- 최댓값 삭제  
    max heap에서 root의 값이 유효한지 검사하고 유효한 값이 나올 때까지 pop
    
- 최솟값 삭제  
    min heap에서 root의 값이 유효한지 검사하고 유효한 값이 나올 때까지 pop

## 🙂 마무리

