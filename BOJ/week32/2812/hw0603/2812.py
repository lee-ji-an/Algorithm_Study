import sys

N, K = map(int, sys.stdin.readline().strip().split())
num = list(map(int, list(sys.stdin.readline().strip())))
stack = []
pop_cnt = 0

for digit in num:
    while (stack and stack[-1] < digit and pop_cnt < K):
        stack.pop()
    stack.append(digit)

print(''.join(map(str, stack[:N-K])))  # K개만큼 pop 안됐을 경우에는 slice 해 줌
