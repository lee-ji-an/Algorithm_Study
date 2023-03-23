import sys
input = sys.stdin.readline
n = int(input())

result = 0
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = dict()
for a in A:
    for b in B:
        if a + b not in ab:
            ab[a+b] = 1
        else:
            ab[a+b] += 1


for c in C:
    for d in D:
        v = -1 * (c + d)
        if -(c+d) in ab.keys():
            result += ab[v]

print(result)