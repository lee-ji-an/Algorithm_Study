import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


def logic(힙, 힙뺀거, 신호):
    try:
        숫자 = (1, -1)[신호] * heapq.heappop(힙)
        while 힙뺀거[숫자] > 0:      # 최댓값 힙에서 해당 값을 1번 이상 뺀 적이 있다면
            힙뺀거[숫자] -= 1        # 동일한 숫자를 2~3번 뺐을 수도 있으니, 1만 빼서 중복 관리
            숫자 = (1, -1)[신호] * heapq.heappop(힙)
        return 숫자
    except IndexError:
        return 'F'


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        minheap = []        # 최솟값 힙
        maxheap = []        # 최댓값 힙
        minheap_del = defaultdict(int)      # 최솟값 힙에서 어떤 값을 뺐는지
        maxheap_del = defaultdict(int)      # 최댓값 힙에서 어떤 값을 뺐는지
        cnt = 0        # 현재 힙에 있는 숫자의 개수
        k = int(input())
        for _ in range(k):
            inst, num = input().split()
            num = int(num)
            if inst == 'I':
                heapq.heappush(minheap, num)
                heapq.heappush(maxheap, -num)
                cnt += 1
            else:
                if cnt > 0:     # 들어간 게 더 많을 때
                    if num == -1:
                        minheap_del[logic(minheap, maxheap_del, 0)] += 1       # 최솟값 힙에서 해당 숫자를 뺐음
                    else:
                        maxheap_del[logic(maxheap, minheap_del, 1)] += 1
                    cnt -= 1       # 힙에서 숫자 하나를 뺐으므로, cnt_를 -1함

        if cnt > 0:
            min_flag = logic(minheap, maxheap_del, 0)
            max_flag = logic(maxheap, minheap_del, 1)

            if max_flag == 'F':
                print(min_flag, min_flag)
            elif min_flag == 'F':
                print(max_flag, max_flag)
            else:
                print(max_flag, min_flag)
        else:
            print('EMPTY')
