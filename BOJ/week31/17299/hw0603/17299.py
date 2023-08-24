from collections import Counter
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
F = Counter(arr)
stack = []
result = ["-1"] * N

for i, val in enumerate(arr):
    # 현재 stack top의 F값이 val의 F값보다 작으면 반복 -> 오등큰수의 정의
    while (stack and F[arr[stack[-1]]] < F[val]):
        result[stack.pop()] = str(val)
    stack.append(i)

print(' '.join(result))
