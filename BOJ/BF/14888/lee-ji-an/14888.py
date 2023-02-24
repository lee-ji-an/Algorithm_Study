import sys
input = sys.stdin.readline

PLUS, MINUS, MULTIPLY, DIVIDE = 0, 1, 2, 3

N = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

max_value, min_value = -1 * float('inf'), float('inf')


def dfs(depth, value):
    global max_value, min_value
    if depth == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return
    if op_list[PLUS] > 0:
        op_list[PLUS] -= 1
        dfs(depth + 1, value + num_list[depth])
        op_list[PLUS] += 1
    if op_list[MINUS] > 0:
        op_list[MINUS] -= 1
        dfs(depth + 1, value - num_list[depth])
        op_list[MINUS] += 1
    if op_list[MULTIPLY] > 0:
        op_list[MULTIPLY] -= 1
        dfs(depth + 1, value * num_list[depth])
        op_list[MULTIPLY] += 1
    if op_list[DIVIDE] > 0:
        op_list[DIVIDE] -= 1
        if num_list[depth] * value < 0:
            dfs(depth + 1, (abs(value) // abs(num_list[depth])) * -1)
        else:
            dfs(depth + 1, value // num_list[depth])
        op_list[DIVIDE] += 1


dfs(1, num_list[0])
print(max_value)
print(min_value)
