from collections import defaultdict
import sys

N = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = defaultdict(int)  # 배열 A와 B로 만들 수 있는 모든 합
for i in range(N):
    for j in range(N):
        AB[A[i] + B[j]] += 1  # 경우의 수 저장

answer = 0
CD_sum = (C[i] + D[j] for i in range(N) for j in range(N))  # C, D로 만들 수 있는 합들의 제네레이터
# AB 딕셔너리에 -(C+D) 가 있는지 확인
for s in CD_sum:
    if (-s in AB):
        answer += AB[-s]
print(answer)
