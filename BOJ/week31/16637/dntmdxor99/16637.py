import sys
from collections import deque
input = sys.stdin.readline


def calculate(dq : deque()):
    while len(dq) > 1:
        dq.appendleft(str(eval(dq.popleft() + dq.popleft() + dq.popleft())))
    return dq.popleft()
        

def choice(cnt):
    global maxNum
    for a in range(1, n, 2):
        num1 = str(eval(''.join(maps[a - 1 : a +  2])))
        if cnt == 1:
            maxNum = max(maxNum, int(calculate(deque(maps[:a - 1] + [num1] + maps[a + 2:]))))
        if cnt >= 2:
            for b in range(a + 4, n, 2):
                num2 = str(eval(''.join(maps[b - 1 : b + 2])))
                if cnt == 2:
                    maxNum = max(maxNum, int(calculate(deque(
                        maps[: a - 1] + [num1] + 
                        maps[a + 2 : b - 1] + [num2] + 
                        maps[b + 2 :]
                        ))))
                if cnt >= 3:
                    for c in range(b + 4, n , 2):
                        num3 = str(eval(''.join(maps[c - 1 : c + 2])))
                        if cnt == 3:
                            maxNum = max(maxNum, int(calculate(deque(
                                maps[: a - 1] + [num1] + 
                                maps[a + 2 : b - 1] + [num2] + 
                                maps[b + 2 : c - 1] + [num3] + 
                                maps[c + 2 :]
                                ))))
                        if cnt >= 4:
                            for d in range(c + 4, n, 2):
                                num4 = str(eval(''.join(maps[d - 1 : d + 2])))
                                if cnt == 4:
                                    maxNum = max(maxNum, int(calculate(deque(
                                        maps[: a - 1] + [num1] + 
                                        maps[a + 2 : b - 1] + [num2] + 
                                        maps[b + 2 : c - 1] + [num3] + 
                                        maps[c + 2 : d - 1] + [num4] + maps[d + 2 :]))))
                                if cnt >= 5:
                                    for e in range(d + 4, n, 2):
                                        num5 = str(eval(''.join(maps[e - 1 : e + 2])))
                                        if cnt == 5:
                                            maxNum = max(maxNum, int(calculate(deque(
                                                maps[: a - 1] + [num1] + 
                                                maps[a + 2 : b - 1] + [num2] + 
                                                maps[b + 2 : c - 1] + [num3] + 
                                                maps[c + 2 : d - 1] + [num4] + 
                                                maps[d + 2 : e - 1] + [num5] + 
                                                maps[e + 2 : ]
                                                ))))


if __name__ == "__main__":
    n = int(input())
    maps = list(input().strip())
    maxNum = int(calculate(deque(maps)))
    
    for cnt in range(1, n // 4 + 1):
        choice(cnt)
    
    print(maxNum)