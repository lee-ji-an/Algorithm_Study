import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
number = list(map(int, input().rstrip()))
stack = []

for num in number:
    while stack and stack[-1] < num and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)

for _ in range(k):
    stack.pop()

print(*stack, sep="")