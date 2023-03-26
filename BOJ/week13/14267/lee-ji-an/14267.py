import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())
boss = list(map(int, input().split()))

adj = defaultdict(list)
praise = [0] * (N + 1)
ans = [0] * (N + 1)

for i in range(M):
    worker, value = map(int, input().split())
    praise[worker] += value

for i in range(N):  # adj 에 부하 직원을 저장
    adj[boss[i]].append(i + 1)


def solve():
    q = deque([(1, 0)])  # 부모노드 부터 시작해서 자식노드까지 모든 노드를 탐색해서 칭찬 점수를 누적
    while q:
        worker, value = q.popleft()
        ans[worker] = value
        for w in adj[worker]:
            q.append((w, value + praise[w]))


solve()
for i in range(1, N + 1):
    print(ans[i], end=" ")
