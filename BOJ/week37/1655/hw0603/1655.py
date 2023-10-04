import heapq
import sys

N = int(sys.stdin.readline())
maxHeap, minHeap = [], []
result = []

heapq.heappush(minHeap, int(sys.stdin.readline()))
result.append(minHeap[0])

def balance(maxheap, minheap):
    while (-maxheap[0] > minheap[0]):
        a = -heapq.heappop(maxheap)
        b = heapq.heappop(minheap)
        heapq.heappush(minheap, a)
        heapq.heappush(maxheap, -b)

for length in range(2, N+1):  # length는 해당 시행에서 삽입 후의 길이 기준
    num = int(sys.stdin.readline())

    if (length & 1):
        heapq.heappush(minHeap, num)
    else:
        heapq.heappush(maxHeap, -num)
    

    balance(minHeap, maxHeap)

    if (length & 1):  # 길이가 홀수
        result.append(minHeap[0])
    else:
        result.append(min(minHeap[0], -maxHeap[0]))
    

print(*result, sep='\n')