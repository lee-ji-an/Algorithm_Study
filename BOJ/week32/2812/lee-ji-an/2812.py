import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = input().rstrip()

digit = N - K
stack = [0] * (N - K)
top = -1

for i in range(N):
    num = number[i]

    # num 보다 작은 숫자는 모두 stack 에서 pop
    while top >= 0:
        # 현재 stack 에 담긴 숫자로 원래 숫자의 길이를 만들 수 없을 때 / stack의 top이 가리키고 있는 숫자가 num 보다 작을 때 -> break
        if top + N - i < digit or stack[top] >= num:
            break
        top -= 1

    # 원래 숫자 길이보다 작을 때만 num 을 stack에 append
    if top + 1 < digit:
        top += 1
        stack[top] = num

print(''.join(map(str, stack)))
