import sys
import heapq

input = sys.stdin.readline

p_num = int(input())

for _ in range(p_num):
    N = int(input())
    min_heap = []
    max_heap = []
    pop_set = set()
    for i in range(N):
        data = input().split()
        operation, num = data[0], int(data[1])
        if operation == 'I':
            # 삽입 데이터로 같은 수가 나왔을 때 이를 구분하기 위해서 i 를 함께 저장
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, -i))
        else:  # D 연산
            if num == 1:  # 최댓값 삭제
                # 유효한 최댓값이 나올 때까지 pop
                while max_heap and (-max_heap[0][0], -max_heap[0][1]) in pop_set:
                    heapq.heappop(max_heap)
                if max_heap:
                    number, order = heapq.heappop(max_heap)
                    pop_set.add((-number, -order))
            else:  # 최솟값 삭제
                # 유효한 최솟값이 나올 때까지 pop
                while min_heap and (min_heap[0][0], min_heap[0][1]) in pop_set:
                    heapq.heappop(min_heap)
                if min_heap:
                    number, order = heapq.heappop(min_heap)
                    pop_set.add((number, order))

    while max_heap and (-max_heap[0][0], -max_heap[0][1]) in pop_set:
        heapq.heappop(max_heap)
    while min_heap and (min_heap[0][0], min_heap[0][1]) in pop_set:
        heapq.heappop(min_heap)

    if not (min_heap and max_heap):
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
