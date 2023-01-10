import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

antic = ['a', 'n', 't', 'i', 'c']
rest = list(set([chr(i) for i in range(97, 123)]) - set(antic))
ans = float('-inf')

words = [0] * n
for i in range(n):
    tmp = input().rstrip()
    for t in tmp:
        words[i] |= (1 << (ord(t) - 97))

if k < 5:
    print(0)
    exit()

combi = list(combinations(rest, k-5))

for c in combi:
    learned = 532741
    cnt = 0

    for i in c:
        learned |= (1 << ord(i) - 97)

    for word in words:
        if word & learned == word:
            cnt += 1
    ans = max(cnt, ans)

print(ans)