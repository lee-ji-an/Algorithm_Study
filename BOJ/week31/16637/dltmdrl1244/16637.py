import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 바로 인접한 숫자 (괄호가 서로 붙어있어 중첩된 경우)가 있는지 검사
def is_valid(combi):
    for i in range(len(combi) - 1):
        if combi[i] + 1 == combi[i+1]:
            return False
    return True

# 괄호가 있으면 합치고 아니면 그냥 넣어서 최종적으로 계산할 숫자의 배열을 만듦
def make_operand(is_bracket):
    t = deque()

    operand_idx = 0
    operator_idx = 0
    while operand_idx < len(operand) and operator_idx <= len(operator):

        if is_bracket[operator_idx]:
            if operator[operator_idx] == '+':
                t.append(operand[operand_idx] + operand[operand_idx + 1])

            elif operator[operator_idx] == '-':
                t.append(operand[operand_idx] - operand[operand_idx + 1])

            else:
                t.append(operand[operand_idx] * operand[operand_idx + 1])

            operand_idx += 1
            operator_idx += 1

        else:
            t.append(operand[operand_idx])

        operand_idx += 1
        operator_idx += 1

    return t


n = int(input())
string = list(input().rstrip())
operand = []
operator = []
ans = -999999999999999

for i in range(0, n, 2):
    operand.append(int(string[i]))

for i in range(1, n, 2):
    operator.append(string[i])

for c in range(len(operator) + 1):
    for combi in combinations([i for i in range(len(operator))], c):
        if not is_valid(combi):
            continue

        # 괄호가 쳐진 연산자는 is_bracket이 True
        is_bracket = [False] * len(operator)
        for c in combi:
            is_bracket[c] = True
        is_bracket.append(False)

        q = make_operand(is_bracket)

        for i in range(len(operator)):
            if not is_bracket[i]:
                a = q.popleft()
                b = q.popleft()

                if operator[i] == '+':
                    q.appendleft(a + b)
                elif operator[i] == '-':
                    q.appendleft(a - b)
                else:
                    q.appendleft(a * b)
        
        ans = max(ans, q[0])

print(ans)