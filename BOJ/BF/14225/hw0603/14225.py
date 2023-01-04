from itertools import combinations
import sys

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split(' ')))

data = [False] * (sum(S)+1)  # 최대로 나올 수 있는 합
data[0] = True

for i in range(1, N+1): # 1~N개
    for j in combinations(S, i): # S에서 1~N개를 뽑는 경우
        data[sum(j)] = True # 나올 수 있는 합에 True 기록

try:
    print(data.index(False))
except ValueError:
    print(sum(S)+1)
