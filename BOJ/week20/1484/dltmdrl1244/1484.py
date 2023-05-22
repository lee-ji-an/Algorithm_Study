import sys
input = sys.stdin.readline

n = int(input())
'''
(now - memory)(now + memory) == n
좌항이 n보다 크면 memory += 1 (결과를 더 작게 함)
좌항이 n보다 작으면 now += 1 (결과를 더 크게 함)
'''
now = 1
memory = 1
answer = []

while now == 1 or now > memory:
    t = (now - memory) * (now + memory)
    if t == n:
        answer.append(now)
        memory += 1
        now += 1
    elif t > n:
        memory += 1
    else:
        now += 1

if answer:
    print(*answer, sep="\n")
else:
    print(-1)