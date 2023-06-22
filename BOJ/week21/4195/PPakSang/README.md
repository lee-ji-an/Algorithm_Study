## Info
[4195 친구 네트워크](https://www.acmicpc.net/problem/4195)

## 💡 풀이 방법 요약
> 동적으로 노드가 생기는 union find
> 
> 새로운 노드 생길 때마다 (group id, 노드 이름):식별자, (노드 이름, group id):group, (group id, 1):size 정보 저장
> 
> 두 노드를 같은 그룹으로 묶는데 이를 위해서 두 노드의 그룹 확인
> 
> 그룹 확인: 두 노드의 현재 그룹이 본인의 원래 그룹이었는지 확인 
> -> 아니면 현재 그룹의 식별자를 이용해 또 그룹 확인 (find 과정), 현재 그룹이 본인의 원래 그룹이다는 것은 그룹의 대표라는 것 
> 
> 그룹 합치기: 두 그룹 정보 나오면, group 데이터를 수정해서 그룹 병합 (이 때 기존 그룹 대표의 그룹 번호를 변경해야함)
> 
> 그룹 합칠 때 두 그룹의 사이즈도 병합 (이미 같은 그룹이라면 합치면 안됨)

## 🙂 마무리