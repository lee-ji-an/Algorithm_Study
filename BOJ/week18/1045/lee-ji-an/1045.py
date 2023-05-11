import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adj_list = []
ans = [0] * N
edge_set = set()
extra_cnt = M - (N-1)
parent = [i for i in range(N)]

for i in range(N):
    adj_list.append(input().rstrip())


def root(i):
    while i != parent[i]:
        i = parent[i]
    return i


def connected(p, q):
    return root(p) == root(q)


def union(p, q):
    id1, id2 = root(p), root(q)
    parent[id2] = id1


# union_find 로 N개의 노드를 연결
for i in range(N):
    for j in range(i + 1, N):
        if not connected(i, j) and adj_list[i][j] == 'Y':
            union(i, j)
            edge_set.add((i, j))
            ans[i] += 1
            ans[j] += 1

# 모든 노드가 모두 연결돼 있는지 확인
flag = True
root_idx = root(0)
for i in range(1, N):
    if root_idx != root(i):
        print(-1)
        flag = False
        break

if flag:
    # 남은 edge 들을 추가
    for i in range(N):
        if extra_cnt <= 0:
            break
        for j in range(i + 1, N):
            if extra_cnt <= 0:
                break
            if adj_list[i][j] == 'Y' and (i, j) not in edge_set:
                edge_set.add((i, j))
                ans[i] += 1
                ans[j] += 1
                extra_cnt -= 1

    if extra_cnt == 0:
        print(' '.join(map(str, ans)))
    else:
        print(-1)
