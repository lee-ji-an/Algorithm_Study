import sys

def find(x):
    if (x == parent[x]):
        return x  # 최상위 노드면 그대로 반환
    
    parent[x] = find(parent[x])  # 최상위 노드로 갱신
    return parent[x]
    
def union(x, y):
    x, y = find(x), find(y)  # 각 친구의 부모노드 찾음
    if (x != y):
        parent[y] = x  # 부모가 다른 경우 합침
        friendCnt[x] += friendCnt[y]  # 합친 후 친구 수 더함


for _ in range(int(sys.stdin.readline())):
    parent = {}
    friendCnt = {}

    F = int(sys.stdin.readline())  # F: 친구 관계의 수
    for _ in range(F):
        p1, p2 = sys.stdin.readline().split()

        # 친구 관계가 없는 사람이라면 초기화(자기 자신을 부모로 설정)
        for p in (p1, p2):
            if (p not in parent):
                parent[p] = p
                friendCnt[p] = 1

        union(p1, p2)  # 두 사람의 친구 관계 합침

        print(friendCnt[find(p1)])
