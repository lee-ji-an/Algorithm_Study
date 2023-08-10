import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
hq = []
result = []

for m in range(M):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)  # num1 -> num2
    in_degree[num2] += 1

# inDegree 가 0 인 node 를 찾아 heapq 에 넣어 초기 세팅
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(hq, i)

while hq:
    num = heapq.heappop(hq)
    result.append(num)  # 정답 배열에 넣기

    for node in graph[num]:  # num 이 가리키고 있었던 곳을 탐색
        in_degree[node] -= 1
        if in_degree[node] == 0:
            heapq.heappush(hq, node)

print(*result)
