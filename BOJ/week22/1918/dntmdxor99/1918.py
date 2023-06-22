import sys
input = sys.stdin.readline


if __name__ == "__main__":
    maps = list(input().strip())
    pri = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : -1, ')' : -1}

    operator = []       # 연산자 스택
    operand = []        # 피연산자 스택

    for i in maps:
        if i.isalpha():
            operand.append(i)       # 피연산자는 그대로 넣음
        else:
            if i == ')':        # 여는 괄호까지 팝해서 넣음
                while operator[-1] != '(':
                    operand.append(operator.pop())
                operator.pop()
            elif i == '(':      # 여는 괄호는 그냥 넣음
                operator.append(i)
            else:
                while operator:     # 연산자 스택에 값이 있다면
                    if pri[i] <= pri[operator[-1]]:     # 앞선 애보다 우선 순위가 낮거나 같으면 팝하면 됨
                        operand.append(operator.pop())
                    else:
                        break
                operator.append(i)

    while operator:     # 남은 애들 다 처리하면 끝
        operand.append(operator.pop())
    print(''.join(operand))