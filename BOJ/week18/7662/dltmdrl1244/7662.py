import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    minheap = []
    maxheap = []
    min_dict = dict()
    max_dict = dict()
    max_count = 0
    n = int(input())
    for i in range(n):
        op, num = input().split()
        num = int(num)
        if op == 'I': # 삽입
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)

        else: # 삭제
            if num == -1: # 최솟값 삭제
                if len(minheap) - max_count > 0:
                    minval = heapq.heappop(minheap)
                    # minval이 'D -1' 에 의해 이미 삭제됐어야 하는 값인지 검증
                    while minval in max_dict and max_dict[minval] > 0:
                        # 올바른 minval이 나올 때까지 반복
                        max_dict[minval] -= 1
                        max_count -= 1
                        minval = heapq.heappop(minheap)
                    
                    # 'D 1'을 하였을 때 이미 삭제됐어야 하는 값인지 판별하기 위한 딕셔너리 업데이트
                    if minval in min_dict:
                        min_dict[minval] += 1
                    else:
                        min_dict[minval] = 1
            else: # 최댓값 삭제
                # num == -1일 때와 똑같은 작업을 반대로 수행해준다
                if len(minheap) - max_count > 0:
                    maxval = -heapq.heappop(maxheap)

                    while maxval in min_dict and min_dict[maxval] > 0:
                        min_dict[maxval] -= 1
                        maxval = -heapq.heappop(maxheap)

                    max_count += 1

                    if maxval in max_dict:
                        max_dict[maxval] += 1
                    else:
                        max_dict[maxval] = 1

    res = []
    # minheap에는 'D 1' (최댓값 삭제 작업)에 의해 삭제됐어야 하는 값이 있을 수도 있다. 이를 검증하면서 res 배열에 옮겨담는다.
    for num in minheap:
        if num in max_dict and max_dict[num] > 0:
            max_dict[num] -= 1
        else:
            res.append(num)
    
    # 만약 res 배열이 비었으면 큐가 빈 것
    if not res:
        print("EMPTY")
    else:
        res.sort()
        print(res[-1], res[0])
    