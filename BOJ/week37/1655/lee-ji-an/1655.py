import sys
import heapq
input = sys.stdin.readline

N = int(input())

number = []
for _ in range(N):
    number.append(int(input()))

left_heap = []  # max heap
right_heap = []  # min heap

for i in range(0, N):
    if i == 0 or -left_heap[0] >= number[i]:
        heapq.heappush(left_heap, -number[i])
    else:
        heapq.heappush(right_heap, number[i])

    # 숫자가 홀수 개일 때
    if i % 2 == 0 and len(left_heap) < len(right_heap):
        num = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -num)
    # 숫자가 짝수 개일 때
    elif i % 2 == 1 and len(left_heap) > len(right_heap):
        num = heapq.heappop(left_heap)
        heapq.heappush(right_heap, -num)

    print(-left_heap[0])

