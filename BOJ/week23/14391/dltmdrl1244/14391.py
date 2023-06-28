import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []
ans = 0
for _ in range(n):
    paper.append(list(map(int, input().rstrip())))

for i in range(2 ** (n*m)):
    score = 0
    for r in range(n):
        rowsum = 0
        for c in range(m):
            idx = r * m + c
            if i & (1 << idx):
                rowsum = rowsum * 10 + paper[r][c]
            else:
                score += rowsum
                rowsum = 0
        score += rowsum
    
    for c in range(m):
        colsum = 0
        for r in range(n):
            idx = r * m + c
            if i & (1 << idx) == 0:
                colsum = colsum * 10 + paper[r][c]
            else:
                score += colsum
                colsum = 0
        score += colsum

    ans = max(ans, score)

print(ans)