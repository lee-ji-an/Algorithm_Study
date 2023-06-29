import sys
input = sys.stdin.readline

string = input().rstrip()
exp = input().rstrip()

# 끝에서부터 exp 길이만큼을 살펴봤을 때 exp와 같다면 모두 pop
def check():
    stacktop = "".join(stack[-(len(exp)-1) - 1:])
    if stacktop == exp:
        for _ in range(len(exp)):
            stack.pop()

# 스택에다가 넣고 폭발 문자열이 있는지 check
stack = []
for st in string:
    stack.append(st)
    check()

if stack:
    print("".join(stack))
else:
    print("FRULA")