import sys
input = sys.stdin.readline

def root(p):
    while p != ids[p]:
        p = ids[p]    
    return p

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    if connected(p, q):
        print(size[root(p)])
        return
    
    a, b = root(p), root(q)
    if size[a] >= size[b]:
        size[a] += size[b]
        ids[b] = a
        print(size[a])
    else:
        size[b] += size[a]
        ids[a] = b
        print(size[b])
    
for _ in range(int(input())):
    n = int(input())
    ids = []
    size = []

    friend_dict = dict()
    friend_id = 0

    for i in range(n):
        v1, v2 = input().split()
        # 새 사람이 들어올 때마다 id, size 생성 및 딕셔너리에 인덱스 저장
        if v1 not in friend_dict:
            friend_dict[v1] = friend_id
            ids.append(friend_id)
            size.append(1)
            friend_id += 1

        if v2 not in friend_dict:
            friend_dict[v2] = friend_id
            ids.append(friend_id)
            size.append(1)
            friend_id += 1
        
        # 유니온 하면서 크기 print
        union(friend_dict[v1], friend_dict[v2])