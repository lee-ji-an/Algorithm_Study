from collections import deque
import sys

N, M = map(int, sys.stdin.readline().strip().split())  # 가수 수, PD 수
deps = {i: set() for i in range(1, N+1)}
inDegree = [0 for _ in range(N+1)]  # 가수별 진입차수(의존성 걸린 횟수)
q = deque()
answer = []

# 의존성 전처리
depTupleList = []
for _ in range(M):
    singerCnt, *data = list(map(int, sys.stdin.readline().split()))  # idx 0은 PD별 담당 가수 수
    for i in range(singerCnt):
        for j in range(i+1, singerCnt):
            depTupleList.append((data[i], data[j]))
for A, B in set(depTupleList):
    deps[A].add(B)  # graph[A]: A가수 때문에 의존성 걸리는 가수들
    inDegree[B] += 1

# 진입차수가 0인 가수(=종속적이지 않은 가수)들을 큐에 모두 삽입
for singerNum in range(1, N+1):
    if (inDegree[singerNum] == 0):
        q.append(singerNum)

# 큐에서 하나씩 pop() 하며 줄 세움
while (q):
    singerNum = q.popleft()
    answer.append(singerNum)

    # singerNum 번 가수에 종속적이였던 가수들에 대하여
    for dep_singerNum in deps[singerNum]:
        inDegree[dep_singerNum] -= 1  # 각 가수들의 진입차수 감소
        if (inDegree[dep_singerNum] == 0):  # 종속성이 완전히 해제된 가수는 큐에 삽입
            q.append(dep_singerNum)


print(*answer if len(answer) == N else [0], sep='\n')
