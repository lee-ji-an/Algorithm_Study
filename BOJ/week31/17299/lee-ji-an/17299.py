import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
cnt_dict = defaultdict(int)
dp = [-1] * (N + 1)
res = [-1] * N
top = -1
stack = [0] * N

# 숫자의 등장 횟수를 구함
for i in range(N):
    cnt_dict[num_list[i]] += 1

# 맨 오른쪽 숫자를 stack 넣고 시작
top += 1
stack[top] = num_list[N - 1]

# 오른쪽에서 왼쪽으로 탐색
for i in range(N-2, -1, -1):
    num = num_list[i]
    # 현재 숫자의 cnt 보다 작거나 같은 수를 pop 하고 나 자신을 push
    while top >= 0:
        if cnt_dict[stack[top]] > cnt_dict[num]:
            break
        top -= 1
    # stack 의 맨 위 숫자를 정답으로 표시
    if top >= 0:
        res[i] = stack[top]

    top += 1
    stack[top] = num

print(*res)
