import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
enable = [False for _ in range(sum(s)+2)]
enable[0] = True

for i in range(n+1):
    combi = combinations(s, i)
    for c in combi:
        enable[sum(c)] = True

print(enable.index(False))