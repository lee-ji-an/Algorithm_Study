import heapq
import sys

N = int(sys.stdin.readline())
data = []
reservation = set()

for _ in range(N):
    p, d = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(data, (-p, d))

def available(day):
    d = day
    while (d in reservation):
        d -= 1
    if (d <= 0):
        return False
    reservation.add(d)
    return True

answer = 0
while (data):
    price, day = heapq.heappop(data)
    if (available(day)):
        answer += price

print(-answer)
