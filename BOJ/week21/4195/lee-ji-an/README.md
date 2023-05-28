## Info
[4195 친구 네트워크](https://www.acmicpc.net/problem/4195)

## 💡 풀이 방법 요약
> UF 이용

새로운 친구 관계가 나올 때마다 UF를 수행
- Union 을 수행할 때마다 size(내가 속한 그래프의 노드 갯수)를 갱신함

```Python
    if size[id1] > size[id2]:
        parent[id2] = id1
        size[id1] += size[id2]
    else:
        parent[id1] = id2
        size[id2] += size[id1]
```
size 비교를 통해 트리의 depth를 줄이고 친구의 수도 알맞게 유지할 수 있다!


## 🙂 마무리
