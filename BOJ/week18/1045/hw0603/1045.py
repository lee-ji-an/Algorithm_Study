import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
isConnected = [
    list(map(
        lambda x: True if x == 'Y' else False,
        list(sys.stdin.readline().rstrip())
    )) for _ in range(N)
]
answer = [0] * N  # 정답 배열: answer[i]를 끝점으로 하는 도로의 개수 리스트
heap = []

for i, row in enumerate(isConnected):
    for j, item in enumerate(row):
        if (item and i < j):
            heapq.heappush(heap, (i, j))

parents = [i for i in range(N)]
def find(node):
    parents[node] = find(parents[node]) if parents[node] != node else node
    return parents[node]


def union(n1, n2):
    root1, root2 = find(n1), find(n2)
    if (root1 == root2):
        return False
    else:
        parents[root2] = root1
        return True

# 존재하는 간선 개수가 M보다 작으면 연결할 수 없음
if (len(heap) < M):
    sys.exit(print(-1))

# 1. MST 만들면서 (N-1)개의 간선을 정답 배열에 추가
edge_cnt = 0
mst_heap = []
while (heap):
    node1, node2 = heapq.heappop(heap)
    if (union(node1, node2)):
        answer[node1] += 1
        answer[node2] += 1
        edge_cnt += 1
    else:
        heapq.heappush(mst_heap, (node1, node2))
# MST가 형성되지 않았다면 모두 연결할 수 없음
if (edge_cnt != N-1):
    sys.exit(print(-1))

# 2. 부족한 M-(N-1) 개의 간선을 우선 순위에 맞게 추가
for _ in range(M-edge_cnt):
    n1, n2 = heapq.heappop(mst_heap)
    answer[n1] += 1
    answer[n2] += 1

print(*answer)
