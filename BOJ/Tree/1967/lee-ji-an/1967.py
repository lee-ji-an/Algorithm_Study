import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

parent = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
leaf_nodes = set([i for i in range(1, N + 1)])


for i in range(N - 1):  # 노드가 N인 트리의 간선은 N-1 개
    v, w, weight = map(int, input().split())
    adj[v].append((w, weight))
    adj[w].append((v, weight))


def dfs(v, distance):
    for w, weight in adj[v]:
        if value_list[w] == -1:
            value_list[w] = distance + weight
            dfs(w, distance + weight)


# root 에서 길이가 가장 먼 노드를 구함
value_list = [-1] * (N + 1)
value_list[1] = 0
dfs(1, 0)

# 'root 에서 길이가 가장 먼 노드' 에서 길이가 가장 먼 노드까지 거리 -> 트리의 지름
start = value_list.index(max(value_list))
value_list = [-1] * (N + 1)
value_list[start] = 0
dfs(start, 0)

print(max(value_list))

