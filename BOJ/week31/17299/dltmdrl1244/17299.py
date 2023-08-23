import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
count = {}
stack = []
answer = [-1 for _ in range(n)]

# 각 숫자가 나온 횟수를 기록
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in range(n-1, -1, -1):
    while stack and stack[-1][1] < count[arr[i]] + 1:
        stack.pop()
    
    if stack:
        answer[i] = stack[-1][0]
        
    stack.append((arr[i], count[arr[i]]))


print(*answer)