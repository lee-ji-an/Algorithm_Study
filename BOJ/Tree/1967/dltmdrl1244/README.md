## Info
[1967 - 트리의 지름](https://www.acmicpc.net/problem/1967)

## 💡 풀이 방법 요약
> DFS 2번
- 시작 루트 노드에서 DFS를 수행하여 가장 멀리 떨어진 점을 찾는다.
- 그 점에서부터 다시 DFS를 수행하여 가장 멀리 떨어진 점과의 거리를 찾는다.
- 그 거리가 정답

## 🙂 마무리
[구사과 블로그](https://koosaga.com/14) 에서 찾았는데... 생각 못 할 거 같다.

아래는 내가 처음 푼 코드인데 자꾸 34%에서 틀렸다고 떴다.
- 어떤 노드의 자식 노드들 중에서 가장 긴 줄기를 재귀적으로 리턴
- 이 때 자식 노드가 2개 이상일 때는 줄기들 중에 가장 큰 두 줄기의 합이 답일 가능성이 있다
```python
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
if n == 1:
    print(0)
    exit()
graph = [[] for _ in range(n+1)]
ans = 0
memo = [0] * (n+1)
for _ in range(n-1):
    p, q, w = map(int, input().split())
    graph[p].append((q, w))


def recur(start):
    global ans

    if memo[start]:
        return memo[start]
    
    if not graph[start]:
        return 0

    else:
        t = []
        for nxt in graph[start]:
            t.append(recur(nxt[0]) + nxt[1])
        
        t.sort()        
        if len(t) >= 2:
            ans = max(ans, t[-1] + t[-2])
        memo[start] = t[-1]        
        return t[-1]
    
recur(1)
print(ans)
```