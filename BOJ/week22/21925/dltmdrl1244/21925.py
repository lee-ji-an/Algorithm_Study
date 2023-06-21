import sys
input = sys.stdin.readline

def check(idx):
    for i in range(len(stack)):
        if idx + i >= n or stack[len(stack) - 1 - i] != arr[idx + i]:
            return False
    
    return True

n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = 0
i = 0

while i < n:
    # 스택이 비어있거나 가장 위의 값과 다를 경우에는 그냥 넣음
    if not stack or stack[-1] != arr[i]:
        stack.append(arr[i])
        i += 1

    else:
        # 스택에 들어있는 값들과 i번째 이후의 배열들이 팰린드롬을 이룰 경우 ans += 1 하고 그 위치로 이동 (len(stack) 만큼 더해줌)
        if check(i):
            i += len(stack)
            ans += 1
            stack.clear()
        
        # 그렇지 않을 경우 일단 스택에 넣음
        else:
            stack.append(arr[i])
            i += 1

# 스택이 비어있지 않거나, ans가 0이면 -1
print(ans if ans > 0 and not stack else -1)