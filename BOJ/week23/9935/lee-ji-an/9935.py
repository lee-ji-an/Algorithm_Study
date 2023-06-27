import sys
input = sys.stdin.readline

S = input().rstrip()
bomb = input().rstrip()

stack = [0] * len(S)
top = -1
match_idx = -1
flag = False

for i in range(len(S)):
    # 어느 idx 까지 맞았는지 저장
    if S[i] == bomb[match_idx + 1]:
        match_idx += 1
    elif S[i] == bomb[0]:
        match_idx = 0
    else:
        match_idx = -1

    # stack에 저장
    top += 1
    stack[top] = (S[i], match_idx)

    # 폭발 문자열을 만났을 때
    if match_idx == len(bomb) - 1:
        if top - len(bomb) >= 0:
            top -= len(bomb)
            match_idx = stack[top][1]
        else:
            match_idx = -1
            top = -1

if top != -1:
    for i in range(top + 1):
        print(stack[i][0], end="")
else:
    print("FRULA")
