from collections import deque

def solution(x, y, n):
    # Edge
    if (x == y):
        return 0

    visited = set()
    q = deque()
    q.append(x)

    opCnt = 0
    while (q):
        for _ in range(len(q)):
            num = q.popleft()

            for nextNum in (num+n, num*2, num*3):
                if (nextNum in visited):
                    continue

                if (nextNum > y):
                    continue

                if (nextNum == y):
                    return opCnt+1

                visited.add(nextNum)
                q.append(nextNum)

        opCnt += 1

    return -1
