import itertools
n, s = map(int, input().split())
board = list(map(int, input().split()))
cnt = 0
for i in range(1, n + 1):
    for j in itertools.combinations(board, i):
        if sum(j) == s:
            cnt += 1
print(cnt)