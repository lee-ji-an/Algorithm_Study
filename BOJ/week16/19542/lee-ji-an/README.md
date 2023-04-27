## Info
[19542 전단지 돌리기](https://www.acmicpc.net/problem/19542)

## 💡 풀이 방법 요약
1. bfs 탐색으로 부모 노드와 depth 를 구함
2. leaf node로부터의 거리를 구함 
- 이때 leaf node와의 거리 중 가장 긴 거리를 구해야 함 
- 따라서, 가장 depth가 깊은 노드부터 거리를 구하고 이미 거리가 기록돼있으면 종료하는 방식
3. dfs 탐색으로 이동해야 하는 거리 구하기

```Python
ans = N-1
for i in range(1, N+1):
    if dist_list[i] < D:
        ans -= 1

print(max(0, ans*2))
```
dfs 대신에 이렇게 구해도 됨
## 🙂 마무리


