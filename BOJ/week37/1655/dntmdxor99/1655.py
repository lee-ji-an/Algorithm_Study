import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    leftHq = []
    rightHq = []

    for _ in range(n):
        x = int(input())
        
        if len(leftHq) == len(rightHq):
            heapq.heappush(leftHq, -x)
        else:
            heapq.heappush(rightHq, x)
            
        if leftHq and rightHq and leftHq[0] * -1 > rightHq[0]:
            max_value = heapq.heappop(leftHq)
            min_value = heapq.heappop(rightHq)
            
            heapq.heappush(leftHq, min_value * -1)
            heapq.heappush(rightHq, max_value * -1)

        print(leftHq[0] * -1)