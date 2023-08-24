import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
res = []

for m in range(M):
    num1, num2 = map(int, input().split())
    adj[num1].append(num2)
    indegree[num2] += 1

q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    res.append(num)
    for n in adj[num]:
        indegree[n] -= 1
        if indegree[n] == 0:
            q.append(n)

print(*res)
