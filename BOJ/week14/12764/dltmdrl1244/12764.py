import sys
import heapq
input = sys.stdin.readline

n = int(input())
timelist = []
for i in range(n):
    a, b = map(int, input().split())
    timelist.append([a, i])
    timelist.append([b, i])
timelist.sort()

dic = dict() # 몇번 사용자가 몇번 pc를 쓰고 있는지
using = set() # 사용중인 사용자
max_com = -1 # 사용한 적 있었던 마지막 pc 번호 (번호는 0번부터, 즉 필요한 총 pc 대수 - 1)
computers = [] # 각 pc가 사용된 횟수
heap = [] # 쓰고 사용가능해진 pc 리스트

for time, idx in timelist:
    # idx : 들어온 사람의 번호
    if idx not in using: # 사용하고 있지 않다면 (들어옴)
        if not heap: # 사용가능한 pc가 없다면 추가해야 함
            max_com += 1
            computers.append(1)
            using.add(idx) 
            dic[idx] = max_com # idx번째 사람이 max_com번째 pc를 사용중
        else:
            t = heapq.heappop(heap) # 사용가능한 pc 중 번호가 제일 작은 것 뽑기
            using.add(idx)
            computers[t] += 1
            dic[idx] = t
    else: # 나감
        using.remove(idx)
        heapq.heappush(heap, dic[idx])

print(max_com + 1)
print(*computers)
