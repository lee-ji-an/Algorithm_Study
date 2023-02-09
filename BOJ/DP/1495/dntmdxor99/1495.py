from collections import deque
[n, s, m], board = map(int, input().split()), map(int, input().split())
dp = deque([s])
for i in board:
    check = set()
    for _ in range(len(dp)):
        s = dp.popleft()
        for j in [s - i, s + i]:
            if 0 <= j <= m and j not in check:
                dp.append(j)
                check.add(j)
print(max(dp) if len(dp) else -1)