from itertools import combinations
n = int(input())
board = list(map(int, input().split()))
check = [0] * sum(board)
for i in range(1, n + 1):
    for j in combinations(board, i):
        check[sum(j) - 1] = 1
try:
    print(check.index(0) + 1)
except:
    print(len(check) + 1)