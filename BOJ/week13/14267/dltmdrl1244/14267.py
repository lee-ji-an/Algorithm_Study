import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
t = list(map(int, input().split()))
sub = [[] for _ in range(n+1)]
p = [0] * (n+1)
for i in range(1, n):
    sub[t[i]].append(i+1)

def recur(v):
    visited[v] = True
    for nxt in sub[v]:
        if not visited[nxt]:
            recur(nxt)
    
    topo.append(v)

# 위상 정렬
topo = []
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        recur(i)

topo.reverse()

# 칭찬 받은 사원 본인만 우선 기록
for _ in range(m):
    person, amount = map(int, input().split())
    p[person] += amount

# 위상 정렬 순서대로 본인의 직속 상사의 점수를 더해감
for i in range(1, n):
    p[topo[i]] += p[t[topo[i]-1]]

print(*p[1:])