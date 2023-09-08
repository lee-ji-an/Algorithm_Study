## Info
[2623 음악프로그램](https://www.acmicpc.net/problem/2623)

## 💡 풀이 방법 요약
위상 정렬 알고리즘을 통해서 indegree가 0이 되어 선행조건이 모두 해결된 사람을 리스트에 넣어가는 방식으로 진행

재귀를 이용한 방법:
```python
import sys
input = sys.stdin.readline


def dfs(start, vSet):
    visited[start] = True
    vSet.add(start)

    for nxt in graph[start]:
        if nxt in vSet:
            return False

        if not visited[nxt]:
            if not dfs(nxt, vSet):
                return False
    
    vSet.discard(start)
    topo.append(start)
    return True

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    t = list(map(int, input().split()))
    for i in range(1, t[0]):
        graph[t[i]].append(t[i+1])

topo = []
for i in range(1, n+1):
    if not visited[i]:
        if not dfs(i, set()):
            print(0)
            exit(0)

topo.reverse()
print(*topo, sep="\n")


```

## 🙂 마무리
재귀 dfs 하는거보다 indegree 사용하는 게 쉬운 것 같음