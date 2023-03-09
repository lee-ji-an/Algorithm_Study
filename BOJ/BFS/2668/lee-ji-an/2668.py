import sys

input = sys.stdin.readline

N = int(input())
table = [0]
for i in range(N):
    table.append(int(input()))


def dfs():
    max_list = []
    max_cnt = 0
    same = set()
    ans = 0

    for i in range(1, N + 1):
        if i in same:
            continue
        visited = [False] * (N + 1)
        cnt = 0
        pick_list = set()
        idx = i
        while not visited[idx]:
            visited[idx] = True
            idx = table[idx]
            cnt += 1
            pick_list.add(idx)
        if idx == i:
            if len(pick_list.intersection(max_list)) == 0:
                max_cnt += cnt
                max_list = pick_list.union(max_list)
            elif cnt > max_cnt:
                max_cnt = cnt
                max_list = set(pick_list)

    if max_cnt == float('-inf'):
        return ans, list(same)
    else:
        return max_cnt + ans, max_list


cnt, pick_list = dfs()
print(cnt)
pick_list = sorted(list(pick_list))
for item in pick_list:
    print(item)
