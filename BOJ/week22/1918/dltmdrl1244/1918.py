import sys
from collections import deque
input = sys.stdin.readline

# 괄호 없는 문자열 내에서 사칙연산 순서에 맞게 postfix 연산 결과를 문자열 형태로 반환
def make_substring(string):
    operand = deque()
    muldiv = []
    plusminus = []
    for a in string:
        if a in ('+', '-'):
            plusminus.append(a)
        elif a in ('*', '/'):
            muldiv.append(a)
        else: # 피연산자가 들어왔을 때 muldiv (곱셈, 나눗셈) 배열이 비어있지 않다면 그 피연산자는 곱/나눗셈 연산을 해야한다
            if muldiv:
                b = operand.pop()
                # 곱/나눗셈 기호와 직전 피연산자를 함께 이용해서 세 개를 이어 붙인 것을 피연산자 배열에 추가한다
                operand.append(b + a + muldiv.pop())
            else:
                operand.append(a)
    
    # 처리하지 않은 더하기/나누기에 대해서 앞에서부터 연산을 수행하고, 다시 앞에 넣는다.
    for operator in plusminus:
        operand1 = operand.popleft()
        operand2 = operand.popleft()
        operand.appendleft(operand1 + operand2 + operator)
    
    # 한 덩어리가 된 operand를 리턴
    return operand[0]

inputstr = input().rstrip()
stack = []

for st in inputstr:
    if st == ')':
        t = []
        popped = stack.pop()
        while popped != '(':
            t.append(popped)
            popped = stack.pop()
        # 여는 괄호가 나올 때까지 pop 하고, 원래의 순서를 지켜주기 위해 역순으로 make_substring 함수에 넘긴다.
        stack.append(make_substring(t[::-1]))

    else: # 여는괄호 및 연산자, 피연산자는 정상적으로 스택에 넣는다.
        stack.append(st)

# 그리고 괄호 밖의 연산을 수행
print(make_substring(stack))