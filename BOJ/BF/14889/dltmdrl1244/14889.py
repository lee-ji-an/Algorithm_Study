import sys
input = sys.stdin.readline
n = int(input())
score = []
combi = []
ans = float('inf')

def combination(arr, r):
    chosen = []
    def generate(chosen):
        if len(chosen) == r:
            combi.append(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            generate(chosen + [arr[i]])

    generate([])

for _ in range(n):
    score.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i, n):
        score[i][j] += score[j][i]
        score[j][i] = 0

combination([i for i in range(n)], n//2)

for c in combi:
    tmp = 0
    oppo = 0
    opponent = list(set([i for i in range(n)]) - set(c))
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            tmp += score[c[i]][c[j]]

    for i in range(len(c)):
        for j in range(i+1, len(c)):
            oppo += score[opponent[i]][opponent[j]]

    ans = min(ans, abs(tmp - oppo))

print(ans)