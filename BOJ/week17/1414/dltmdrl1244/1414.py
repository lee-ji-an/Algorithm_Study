import sys
input = sys.stdin.readline

def get_weight(char):
    if ord('a') <= ord(char) <= ord('z'):
        return ord(char) - 96
    elif ord('A') <= ord(char) <= ord('Z'):
        return ord(char) - 38 

def root(p):
    while ids[p] != p:
        p = ids[p]
    return p

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    if connected(p, q): return

    id1, id2 = root(p), root(q)
    if size[id1] >= size[id2]:
        size[id1] += size[id2]
        ids[id2] = id1
    else:
        size[id2] += size[id1]
        ids[id1] = id2

n = int(input())
edges = []
ids = [i for i in range(n)]
size = [1 for _ in range(n)]
for i in range(n):
    t = list(input().rstrip())
    for j in range(n):
        if t[j] != '0':
            edges.append((i, j, get_weight(t[j])))

edges.sort(key=lambda x:(x[2]))

answer = 0
count = 0
for n1, n2, weight in edges:
    if n1 == n2 or count == n-1:
        answer += weight
        continue

    if connected(n1, n2):
        answer += weight
    else:
        count += 1
        union(n1, n2)

for i in range(n):
    for j in range(n):
        if not connected(i, j):
            print(-1)
            exit()

print(answer)