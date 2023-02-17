import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

q = deque()
combi = [0] * 6


input_list = list(input().rstrip().split())
while input_list[0] != '0':
    k = input_list[0]
    s = input_list[1:]
    for combi in combinations(s, 6):
        print(' '.join(combi))
    print()
    input_list = list(input().rstrip().split())
