## Info
[7453 - 합이 0인 네 정수](https://www.acmicpc.net/problem/7453)

## 💡 풀이 방법 요약
우선 a와 b를 더해서 하나의 그룹으로 만들었다.  
c, d도 마찬가지로 하고, Counter 함수로 cd를 다시 만들었다.  
ab에 있는 값에 음수를 취해서 cd에 있다면 더했다.

## 🙂 마무리
등수가 높은 코드를 봤는데, 내가 맨 처음 제출했던 방식과 비슷하던데...  
왜 나는 시간 초과가 난지 잘 모르겠다.  

맨 처음 제출했던 방식은 다음과 같다.  
a와 b를 더한 그룹을 ab, c와 d를 더한 그룹을 cd라 하고,  
ab, cd를 정렬했다.  
그리고 음수에서 양수로 넘어가는 지점을 체크하고,  
ab의 음수, cd의 양수를 체크,  
ab의 양수, cd의 음수를 체크했다.  
```python
for i in ab:
    for j in cd:
        if i + j == 0:
            cnt += 1
```
뭐 이런 방식을 사용했다.  
근데 이때 ab가 음수고, cd가 양수일 때,  
저런 반복문에서 더했을 때 양수가 나오면 다시 0이 나올 가능성이 없으므로,  
종료했는데....  
시간 초과가 나서 그냥 다른 방법을 썼다.  