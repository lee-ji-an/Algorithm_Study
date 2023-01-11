import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
min_length = sys.maxsize

start, end = (0, 0)

subtotal = 0
while (start < N):
    if (end == N or subtotal >= S):
        subtotal -= nums[start]
        start += 1
    else:
        subtotal += nums[end]
        end += 1

    if (subtotal >= S):
        min_length = min(min_length, end - start)

print(min_length if min_length <= N else 0)
