import sys

n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]
maxVal = prev = arr.pop(0)
cnt = 0

for num in arr:
    if (num == prev):
        continue

    # 지금 보고 있는 숫자가 prev보다 큰 경우 그 차이만큼 답에 누적해 줌
    if (num > prev):
        cnt += (num - prev)
        maxVal = max(maxVal, num) 
    prev = num

print(cnt + maxVal - prev)
