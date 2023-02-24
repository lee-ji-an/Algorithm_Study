import sys
input = sys.stdin.readline
import math
n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
maxans, minans = float('-inf'), float('inf')


def recur(idx, partsum, operator):
    global maxans, minans
    if idx == n-1:
        maxans = max(maxans, partsum)
        minans = min(minans, partsum)
        return
    
    if operator[0] != 0:
        operator[0] -= 1
        recur(idx + 1, partsum + arr[idx+1], operator)
        operator[0] += 1
    
    if operator[1] != 0:
        operator[1] -= 1
        recur(idx + 1, partsum - arr[idx+1], operator)
        operator[1] += 1
        
    if operator[2] != 0:
        operator[2] -= 1
        recur(idx + 1, partsum * arr[idx+1], operator)
        operator[2] += 1
    
    if operator[3] != 0:
        operator[3] -= 1
        # 소수점을 버려야 하는데 나누는 수가 음수이면 math.ceil 해야하고 양수이면 math.floor 해야한다
        if partsum < 0:
            recur(idx + 1, math.ceil(partsum / arr[idx + 1]), operator)
        else:
            recur(idx + 1, math.floor(partsum / arr[idx + 1]), operator)
        operator[3] += 1

recur(0, arr[0], operator)
print(maxans, minans, sep="\n")