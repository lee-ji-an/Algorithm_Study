## Info
[118667 두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

## 💡 풀이 방법 요약

원형 큐라고 생각하면 매우 편함.  
원형 큐를 만들기 위해서 두 개의 리스트를 합쳐서 하나의 리스트로 만들었음.  
원형 큐에서 두 개의 가림막을 만든다고 생각하면 편함.  
아무튼 그렇게 해서 left, right를 적절하게 연산하면 되고,  
만약 right가 다시 제자리로 돌아온다? 이거는 해결방법이 없는 것임. 내부에 사이클이 존재하므로 -1 반환.  
만약 left가 right를 따라잡는다? 이것 또한 해결 방법이 없는 것이므로 -1 반환.

![Alt text](image.png)

## 🙂 마무리

