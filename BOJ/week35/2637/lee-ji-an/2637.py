import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

relation = [{} for _ in range(N + 1)]
in_degree = [0] * (N + 1)
middle_part = set()

for _ in range(M):
    X, Y, K = map(int, input().split())
    middle_part.add(X)
    in_degree[Y] += 1
    relation[X][Y] = K
ans = {key: value for key, value in relation[N].items()}

# Topological Sort로 부품끼리의 의존 관계를 구함
q = deque()
seq = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    part = q.popleft()
    seq.append(part)
    for ingredient in relation[part].keys():
        in_degree[ingredient] -= 1
        if in_degree[ingredient] == 0:
            q.append(ingredient)

# Topological Sort 순서대로 탐색
for i in range(0, N):
    cur_num = seq[i]
    if cur_num not in middle_part or cur_num not in ans:
        continue

    # cur_num 의 부품을 부품의 재료로 대체
    cnt = ans[cur_num]
    for part, sub_cnt in relation[cur_num].items():
        if part in ans:
            ans[part] += cnt * sub_cnt
        else:
            ans[part] = cnt * sub_cnt
    ans[cur_num] = 0

# 출력
for key in range(1, N + 1):
    if key in middle_part:
        continue
    if key in ans:
        print(key, ans[key])
    else:
        print(key, 0)
