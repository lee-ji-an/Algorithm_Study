import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
height_list = list(map(int, input().split()))

# [ 볼 수 있는 건물의 갯수, 가장 가까운 건물의 번호 ]
ans = [[0, -1] for _ in range(N)]

# 왼쪽을 바라봤을 때
stack = deque([(height_list[0], 0)])
for i in range(1, N):
    # i 번째 건물 높이보다 작거나 같은 건물은 모두 pop
    while stack and stack[0][0] <= height_list[i]:
        stack.popleft()
    # stack 에 원소가 죤재하면 볼 수 있는 건물이 있다는 것
    if stack:
        ans[i][0] += len(stack)
        ans[i][1] = stack[0][1]
    stack.appendleft((height_list[i], i))

# 오른쪽을 바라봤을 때
stack = deque([(height_list[N - 1], N - 1)])
for i in range(N-2, -1, -1):
    while stack and stack[0][0] <= height_list[i]:
        stack.popleft()

    if stack:
        ans[i][0] += len(stack)
        # 이전에 볼 수 있는 건물이 없었거나 더 가까운 건물을 발견했을 때 갱신
        if ans[i][1] == -1 or i - ans[i][1] > stack[0][1] - i:
            ans[i][1] = stack[0][1]
    stack.appendleft((height_list[i], i))

for i in range(N):
    print(f"{ans[i][0]} {ans[i][1] + 1}" if ans[i][0] != 0 else 0)
