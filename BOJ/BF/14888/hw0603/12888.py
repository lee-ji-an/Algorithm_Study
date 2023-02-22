from itertools import permutations
from functools import reduce
import operator
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
opt_list = reduce(operator.add, (([op] * cnt) for op, cnt in zip(['+', '-', '*', '/'], operators)))
max_value, min_value = -sys.maxsize, sys.maxsize

for p in set(permutations(opt_list)):
    num = arr[0]
    for op, nextnum in zip(p, arr[1:]):
        num = int(eval(f"{num}{op}{nextnum}"))
    max_value, min_value = max(max_value, num), min(min_value, num)

print(max_value, min_value, sep='\n')
