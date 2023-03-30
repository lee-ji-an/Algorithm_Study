import sys

n, m = map(int, sys.stdin.readline().split())
superior = [0] + list(map(int, sys.stdin.readline().split()))
score = [0] * (n+1)  # 각 직원들의 칭찬 데이터

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    score[i] += w  # 본인이 직접 칭찬받은 데이터 입력

for i in range(2, n+1):
    score[i] += score[superior[i]]  # 각 직원의 총 칭찬점수는 원래 본인의 점수 + 상사의 점수

# 출력
score.pop(0)
print(*score, sep=' ')
