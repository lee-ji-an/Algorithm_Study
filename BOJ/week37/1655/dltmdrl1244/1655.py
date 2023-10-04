import sys
import heapq
input = sys.stdin.readline

n = int(input())

leftHeap = [] # max heap
rightHeap = [] # min heap
for i in range(n):
    num = int(input())

    # 양쪽 힙에 균형을 맞춰가면서 하나씩 넣어준다. 두 힙의 원소 수는 항상 leftheap이 하나 더 많거나 같다.
    # 그리고 leftheap의 root, 즉 가장 큰 (마이너스를 붙였기 때문에 실제로는 가장 작은) 값이 중간값이 된다.
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)
        
    # rightheap에 있는 값이 더 작으면 안되므로 두 개를 바꿔준다
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        heapq.heappush(leftHeap, -heapq.heappop(rightHeap))
        heapq.heappush(rightHeap, -heapq.heappop(leftHeap))

    print(-leftHeap[0])