import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

N = int(input())
input_list = list(map(int, input().split()))
scv_power = [0] * 3
visited = set()
for i in range(N):
    scv_power[i] = input_list[i]


def bfs():
    q = deque()
    q.append((scv_power[0], scv_power[1], scv_power[2], 0))
    visited.add((scv_power[0], scv_power[1], scv_power[2]))
    while q:
        power1, power2, power3, cnt = q.popleft()
        for attack in permutations([9, 3, 1], 3):
            npower1 = power1 - attack[0] if power1 - attack[0] >= 0 else 0
            npower2 = power2 - attack[1] if power2 - attack[1] >= 0 else 0
            npower3 = power3 - attack[2] if power3 - attack[2] >= 0 else 0
            if (npower1, npower2, npower3) not in visited:
                if npower1 == 0 and npower2 == 0 and npower3 == 0:
                    return cnt + 1
                q.append((npower1, npower2, npower3, cnt + 1))
                visited.add((npower1, npower2, npower3))


print(bfs())
