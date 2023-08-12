import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
ans = 0

for _ in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) != 1:
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    ans += a + b
    heapq.heappush(cards, a + b)

print(ans)