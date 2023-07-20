import sys
import heapq
input = sys.stdin.readline

N = int(input())
card_num = []
ans = 0

for i in range(N):
    heapq.heappush(card_num, int(input()))

while len(card_num) >= 2:
    num1 = heapq.heappop(card_num)
    num2 = heapq.heappop(card_num)
    ans += num1 + num2
    heapq.heappush(card_num, num1 + num2)

print(ans)
