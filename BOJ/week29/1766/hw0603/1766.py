import heapq
import sys

N, M = map(int, sys.stdin.readline().strip().split())  # 문제 개수, 먼저 푸는 것이 좋은 문제 개수
graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]  # 노드별 진입차수
heap = []
answer = []

# 선행문제 정보 기록
for _ in range(M):
    preNo, probNo = map(int, sys.stdin.readline().rstrip().split())
    graph[preNo].append(probNo)
    inDegree[probNo] += 1

# 진입차수가 0인 문제(=종속적이지 않은 문제)들을 우선 큐에 다 넣음
for probNo in range(1, N+1):
    if (inDegree[probNo] == 0):
        heapq.heappush(heap, probNo)

# 우선순위 큐에서 하나씩 꺼내면서 순서대로 문제 풂
while (heap):
    probNo = heapq.heappop(heap)
    answer.append(str(probNo))

    # probNo 번 문제에 종속적이였던 각 문제들에 대해서
    for probNo in graph[probNo]:
        inDegree[probNo] -= 1  # 진입차수 하나 줄임
        if (inDegree[probNo] == 0):  # 종속성이 완전히 해제된 문제는 힙에 push
            heapq.heappush(heap, probNo)


print(" ".join(answer))
