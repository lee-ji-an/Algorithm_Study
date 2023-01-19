from collections import deque
import sys

A, B, C = sorted(map(int, sys.stdin.readline().split()))

q = deque([(A, B, C)])
visited = set()
result = 0

while (q):
    a, b, c = q.popleft()

    if (a == b == c):
        result = 1
        break

    ab = (a-b, b << 1, c) if a > b else (a << 1, b-a, c)
    bc = (a, b-c, c << 1) if b > c else (a, b << 1, c-b)
    ca = (a << 1, b, c-a) if c > a else (a-c, b, c << 1)

    for item in {ab, bc, ca}:
        if (item not in visited):
            visited.add(item)
            q.append(item)

print(result)
