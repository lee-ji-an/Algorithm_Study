import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sumdict = {0: 1}
partsum = [0] * n
t = 0
answer = 0

for idx, item in enumerate(arr):
    t += item
    partsum[idx] = t
    
    # 어느 구간까지 잘라서 k를 만들 수 있는 수가 있으면 더한다
    if (t - k) in sumdict:
        answer += sumdict[t-k]

    # 딕셔너리에 정보 저장
    if t in sumdict:
        sumdict[t] += 1
    else:
        sumdict[t] = 1

print(answer)