import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = -1
left = 0
right = n - 1

while left < right:
    answer = max(answer, min(arr[left], arr[right]) * (right - left - 1))
    
    if arr[left] == arr[right]:
        left += 1
        right -= 1

    elif arr[left] < arr[right] or left + 1 == right:
        left += 1
    else:
        right -= 1

print(answer)