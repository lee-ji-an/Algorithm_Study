import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
disk = [0]
rotation = []

for _ in range(N):
    disk.append(deque(list(map(int, input().split()))))
for _ in range(T):
    x, d, k = map(int, input().split())
    rotation.append((x, d, k))


for i in range(T):
    xi, di, ki = rotation[i]
    if di == 0:                             # 원판 회전
        for dnum in range(xi, N + 1, xi):
            for _ in range(ki):
                disk[dnum].appendleft(disk[dnum].pop())
    else:
        for dnum in range(xi, N + 1, xi):
            for _ in range(ki):
                disk[dnum].append(disk[dnum].popleft())

    flag = False
    del_list = set()
    for j in range(1, N + 1):
        range_list = [n for n in range(j % 2, M, 2)]  # 한 칸씩 띄워서 인접한 숫자를 검사
        if M % 2 == 1 and j % 2 == 1:  # M 이 홀수이고 j가 홀수이면 0을 검사할 숫자에 추가
            range_list.append(0)
        for k in range_list:
            if disk[j][k] == 0:
                continue
            if disk[j][k] == disk[j][(k + 1) % M]:   # 인접한 숫자 비교 -> 바꿔야 할 부분을 set에 집어넣음
                del_list.add((j, k))
                del_list.add((j, (k + 1) % M))
                flag = True
            if disk[j][k] == disk[j][(k - 1) % M]:
                del_list.add((j, k))
                del_list.add((j, (k - 1) % M))
                flag = True
            if j - 1 > 0 and disk[j - 1][k] == disk[j][k]:
                del_list.add((j, k))
                del_list.add((j - 1, k))
                flag = True
            if j + 1 <= N and disk[j + 1][k] == disk[j][k]:
                del_list.add((j, k))
                del_list.add((j + 1, k))
                flag = True
    for item in del_list:   # set에 있는 자리를 0으로 갱신
        disk[item[0]][item[1]] = 0
    if not flag:  # 바뀐 게 없을 때 숫자 갱신
        cnt = 0
        total = 0
        for j in range(1, N + 1):
            for k in range(M):
                if disk[j][k] > 0:
                    cnt += 1
                    total += disk[j][k]
        if cnt == 0:
            break
        avg = total / cnt
        for j in range(1, N + 1):
            for k in range(M):
                if disk[j][k] == 0:
                    continue
                if disk[j][k] > avg:
                    disk[j][k] -= 1
                elif disk[j][k] < avg:
                    disk[j][k] += 1

total = 0
for i in range(1, N + 1):
    total += sum(disk[i])
print(total)
