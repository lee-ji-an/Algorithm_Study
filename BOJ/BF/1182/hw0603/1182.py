from itertools import combinations
import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

print(len([True for i in range(1, N+1) for c in combinations(nums, i) if sum(c) == S]))
