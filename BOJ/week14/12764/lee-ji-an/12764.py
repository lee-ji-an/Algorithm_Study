import heapq
import sys
input = sys.stdin.readline

N = int(input())

start = [0] * N
end = [0] * N
s_ptr = 0
e_ptr = 0
max_computer = 0
cur_computer = 0
heap = []
person_computer = [0] * (N + 1)
computer_cnt = [0] * (N + 1)

for i in range(N):
    s, e = map(int, input().split())
    start[i] = (s, i)
    end[i] = (e, i)

start = sorted(start)
end = sorted(end)

while s_ptr < N or e_ptr < N:
    # 시작 시간일 때
    if s_ptr < N and (e_ptr >= N or start[s_ptr] < end[e_ptr]):
        value, person = start[s_ptr]
        cur_computer += 1
        if cur_computer > max_computer:  # max computer 수가 갱신되었을 때
            max_computer = cur_computer
            person_computer[person] = max_computer
            computer_cnt[max_computer] += 1
        else:  # max computer 수가 갱신되지 않았을 때
            min_computer = heapq.heappop(heap)
            person_computer[person] = min_computer
            computer_cnt[min_computer] += 1
        s_ptr += 1
    # 종료 시간일 때
    else:
        value, person = end[e_ptr]
        cur_computer -= 1
        heapq.heappush(heap, person_computer[person])
        person_computer[person] = -1
        e_ptr += 1

print(max_computer)
for i in range(1, max_computer + 1):
    print(computer_cnt[i], end=" ")
