import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    command = list(input().rstrip())
    l = int(input())
    t = input().rstrip()
    t = t[1:-1]
    err = 0
    if len(t) == 0:
        t = []
    else:
        t = t.split(",")

    q1 = deque(t)
    q2 = deque(t[::-1])
    cur = 0

    for i in command:
        if i == 'R':
            cur += 1
        
        else:
            if len(q1) == 0:
                err = 1
                break
            
            if cur % 2 == 0: 
                q1.popleft()
                q2.pop()
            else:
                q1.pop()
                q2.popleft()

    if err:
        print("error")
    else:
        print("[", end="")
        print(*list(q2) if cur % 2 else q1, sep=",", end="")
        print("]")