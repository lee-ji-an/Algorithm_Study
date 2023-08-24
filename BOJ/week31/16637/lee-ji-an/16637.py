import sys

input = sys.stdin.readline

N = int(input())
formula = input()

ans = float('-inf')


# +, -, * 연산하는 함수
def op(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    else:
        return num1 * num2


def dfs(start, res):
    global ans
    if start >= N:
        ans = max(ans, res)
        return

    # start 에서 괄호를 추가하지 않고 연산
    dfs(start + 2, op(res, int(formula[start + 1]), formula[start]))

    # 괄호를 추가해서 연산
    if start + 3 < N:
        first = op(int(formula[start + 1]), int(formula[start + 3]), formula[start + 2])
        dfs(start + 4, op(res, first, formula[start]))


dfs(1, int(formula[0]))
print(ans)
