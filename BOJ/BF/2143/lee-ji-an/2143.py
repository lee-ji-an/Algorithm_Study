import sys
input = sys.stdin.readline
T = int(input())
lenA = int(input())
A = list(map(int, input().split()))
lenB = int(input())
B = list(map(int, input().split()))
sumA = []
sumB = []
dictA = {}
dictB = {}
total = 0
cnt = 0
for i in range(lenA):
    total = 0
    for j in range(i, lenA):   # dictA를 만듦, (key = A 부분집합에서 나올 수 있는 합 , value = 해당 key의 값이 만들어지는 횟수)
        total += A[j]
        if total in dictA:
            dictA[total] += 1
        else:
            dictA[total] = 1
for i in range(lenB):         # B의 리스트에서 나올 수 있는 합을 모두 탐색 -> dictA에 T-total의 key가 있으면 value를 cnt에 더함
    total = 0
    for j in range(i, lenB):
        total += B[j]
        if T-total in dictA:
            cnt += dictA[T-total]
print(cnt)