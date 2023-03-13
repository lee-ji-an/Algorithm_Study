import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
maxVal = max(arr)
prev = arr.pop(0)
cnt = 0

for num in arr:
    if (num == prev):
        continue
    # 지금 보고 있는 숫자가 prev보다 큰 경우 그 차이만큼 답에 누적해 줌
    if (num > prev):
        cnt += (num - prev)
    prev = num

print(cnt + maxVal - prev)
