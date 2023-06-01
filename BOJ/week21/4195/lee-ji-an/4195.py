import sys
input = sys.stdin.readline

T = int(input())


def root(i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(p, q):
    id1, id2 = root(p), root(q)
    if size[id1] > size[id2]:
        parent[id2] = id1
        size[id1] += size[id2]
    else:
        parent[id1] = id2
        size[id2] += size[id1]


def connected(p, q):
    return root(p) == root(q)


for t in range(T):
    N = int(input())
    parent = [i for i in range(N * 2)]
    size = [1] * (N * 2)
    friend_dict = {}
    friend_cnt = 0
    for n in range(N):
        friend1, friend2 = input().split()
        # 처음 등장한 친구일 때 새롭게 number 를 부여
        if friend1 not in friend_dict:
            friend_dict[friend1] = friend_cnt
            friend_cnt += 1
        if friend2 not in friend_dict:
            friend_dict[friend2] = friend_cnt
            friend_cnt += 1

        friend_num1, friend_num2 = friend_dict[friend1], friend_dict[friend2]
        if not connected(friend_num1, friend_num2):
            union(friend_num1, friend_num2)

        print(size[root(friend_num1)])
