import sys

string = sys.stdin.readline().rstrip()
explode_str = sys.stdin.readline().rstrip()
stack = []

for ch in string:
    stack.append(ch)
    if (len(stack) >= len(explode_str)):
        if (stack[-len(explode_str):] == list(explode_str)):  # 현재 스택이랑 폭발 문자열이랑 같으면
            for _ in range(len(explode_str)):
                stack.pop()  # 폭발

print(''.join(stack) if stack else 'FRULA')
