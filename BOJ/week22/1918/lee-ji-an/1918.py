import sys

input = sys.stdin.readline

infix = input().rstrip()

top = -1
stack = [(0, '')] * len(infix)

# 수가 클수록 계산의 우선순위가 높은 것
def op_priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2


top += 1
stack[top] = (float('-inf'), '')
for i in range(len(infix)):
    if ord('A') <= ord(infix[i]) <= ord('Z'):  # 알파벳인 경우 바로 출력
        print(infix[i], end='')
    else:
        if infix[i] == '(':  # 여는 괄호면 우선순위를 가장 낮게해서 무조건 stack에 push
            top += 1
            stack[top] = (float('-inf'), infix[i])
            continue
        elif infix[i] == ')':  # 닫는 괄호면 여는 괄호 '(' 가 나올 때까지 pop해서 print
            while True:
                if stack[top][1] == '(':
                    top -= 1
                    break
                print(stack[top][1], end='')
                top -= 1
        else:  # +, -, *, / 인 경우 현재 값보다 우선순위가 같거나 높은 것은 pop 하고 현재 연산자를 push
            op_value = op_priority(infix[i])
            while stack[top][0] >= op_value:
                print(stack[top][1], end='')
                top -= 1
            top += 1
            stack[top] = (op_value, infix[i])

while top >= 1:
    print(stack[top][1], end='')
    top -= 1
