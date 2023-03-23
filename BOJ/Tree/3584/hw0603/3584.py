import sys

T = int(sys.stdin.readline())


# 자기 자신으로부터 시작해서 거슬러 올라가면서 루트노트에 도달하기까지의 경로 반환
def getAncestors(parent: list, node: int) -> list[int]:
    result = [node]
    while (parent[node]):
        result.append(parent[node])
        node = parent[node]
    return result


def solve(parent: list, n1: int, n2: int) -> int:
    # 각 노드의 조상 리스트 정의: [node, ..., root]
    n1_ancestors = getAncestors(parent, n1)
    n2_ancestors = getAncestors(parent, n2)

    # 시작 지점(깊이) 맞춰주기(i, j: 각각 n1과 n2 조상 리스트의 시작 인덱스)
    delta = abs(len(n1_ancestors) - len(n2_ancestors))
    i, j = (delta, 0) if len(n1_ancestors) > len(n2_ancestors) else (0, delta)

    # 같은 시작 지점에서 가장 가까운 공통 조상 찾기
    while (n1_ancestors[i] != n2_ancestors[j]):
        i += 1
        j += 1
    assert n1_ancestors[i] == n2_ancestors[j]

    return n1_ancestors[i]

# 테스트 케이스 수 만큼 반복
for _ in range(T):
    N = int(sys.stdin.readline())
    parent = [0] * (N+1)  # idx에 해당하는 노드의 부모들이 기록됨
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        parent[b] = a
    n1, n2 = map(int, sys.stdin.readline().split())  # 가장 가까운 공통 조상을 구할 두 노드

    print(solve(parent, n1, n2))
