import sys
import heapq
input = sys.stdin.readline

N = int(input())

lan_list = [[0] * N for _ in range(N)]
lan_heap = []
adj_set = {k: set() for k in range(0, N)}
visited = [False] * N
min_check = [float('inf')] * N
total_lan_length = 0
required_lan = 0

for i in range(N):
    row = input().rstrip()
    for j in range(N):
        if row[j] == '0':
            lan_length = float('inf')
        else:
            if 'A' <= row[j] <= 'Z':  # A~Z
                lan_length = ord(row[j]) - ord('A') + 27
            else:  # a~z
                lan_length = ord(row[j]) - ord('a') + 1

            total_lan_length += lan_length
            if i != j:
                adj_set[i].add(j)
                adj_set[j].add(i)
        lan_list[i][j] = lan_length

# prim 알고리즘
visited[0] = True
heapq.heappush(lan_heap, (0, 0))
edge_cnt = 0
while lan_heap:
    # heap에서 pop -> MST를 이루는 edge
    length, node = heapq.heappop(lan_heap)
    if not visited[node]:
        visited[node] = True
        edge_cnt += 1
        required_lan += length
    # 인접 노드 탐색
    for adj_node in adj_set[node]:
        if visited[adj_node]:
            continue
        # 메모리 초과 방지 :
        # 1. 현재 heap에 들어있는 node별 최소 길이를 기록해놓고 작을 때만 heap에 넣는다
        # 2. 노드와 노드 사이에 최대 2개의 edge가 있을 수 있으므로 둘의 길이를 비교해서 작은 것을 heap에 넣음
        adj_length = min(lan_list[node][adj_node], lan_list[adj_node][node])
        if min_check[adj_node] > adj_length:
            heapq.heappush(lan_heap, (adj_length, adj_node))
            min_check[adj_node] = adj_length

if edge_cnt < N-1:
    print(-1)
else:
    print(total_lan_length - required_lan)
