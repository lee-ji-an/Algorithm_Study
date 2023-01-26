import math
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def primeChecker():  # 소수 -> True, 소수x -> False 로 체크해서 리스트를 반환
    prime = [True] * 9000
    checker = [True] * (int(math.sqrt(9999)) + 1)
    checker[0], checker[1] = False, False
    for i in range(2, len(checker)):
        if checker[i]:
            for j in range(i + 1, len(checker)):
                if j % i == 0:
                    checker[j] = False
            for j in range(i - (1000 % i), len(prime), i):
                prime[j] = False
    return prime


def changer(totalNumber, digit, n):  # totalNumber의 digit 자리 수를 n으로 바꾸겠다
    s = list(str(totalNumber))
    s[digit] = chr(n + ord('0'))
    return int(''.join(s))


def bfs(old, new):
    q = deque()
    q.append((old, 0))
    visited = {old}
    while q:
        value, cnt = q.popleft()
        if value == new:
            return cnt
        for i in range(3, -1, -1):  # 3, 2, 1, 0
            for j in range(10):
                if j == 0 and i == 0:   # 맨 앞자리가 0인 경우는 pass
                    continue
                newValue = changer(value, i, j)
                if prime[newValue - 1000] and newValue not in visited:
                    visited.add(newValue)
                    q.append((newValue, cnt + 1))
    return -1


prime = primeChecker()
for i in range(T):
    old, new = map(int, input().split())
    res = bfs(old, new)
    if res == -1:
        print("Impossible")
    else:
        print(res)
