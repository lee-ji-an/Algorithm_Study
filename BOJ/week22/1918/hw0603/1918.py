import sys

def infix2postfix(infix_str):
    stack = []
    postfix = ""

    for ch in infix_str:
        if (ch.isalpha()):  # 피연산자(알파벳)의 경우 바로 후위 표기식으로 추가
            postfix += ch
        elif (ch == '('):  # 여는 괄호는 스택에 Push
            stack.append(ch)
        elif (ch == ')'):
            while (stack and stack[-1] != '('):  # 닫는 괄호일 경우 여는 괄호가 나올 때까지 스택에서 pop
                postfix += stack.pop()
            stack.pop()  # 여는 괄호를 스택에서 pop
        else:  # 연산자인 경우 스택의 top에 있는 연산자의 우선순위가 더 높거나 같을 때까지 pop
            assert (ch in priority.keys())
            while (stack and priority[ch] <= priority[stack[-1]]):
                postfix += stack.pop()
            stack.append(ch)
    
    postfix += ''.join(reversed(stack))  # 스택에 남아있는 연산자들을 모두 붙이기

    return postfix


priority = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

print(infix2postfix(sys.stdin.readline().rstrip()))
