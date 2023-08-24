## Info
[2252 줄 세우기](https://www.acmicpc.net/problem/2252)

## 💡 풀이 방법 요약
- 위상 정렬을 사용하면 쉽게 된다

DFS를 사용한 풀이의 예시
```python
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(i):
    global visited, reversetopo
    visited[i] = True
    for nxt in graph[i]:
        if not visited[nxt]:
            dfs(nxt)
    reversetopo.append(i)


visited = [False for _ in range(n+1)]
reversetopo = []
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

reversetopo.reverse()
print(*reversetopo)
```

## 🙂 마무리
주석 참고