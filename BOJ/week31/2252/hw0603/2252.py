from collections import deque
import sys

N, M = map(int, sys.stdin.readline().strip().split())  # 총 학생 수, 의존성 목록 개수
deps = {i: set() for i in range(1, N+1)}
inDegree = [0 for _ in range(N+1)]  # 학생별 진입차수(의존성 걸린 횟수)
q = deque()
answer = []

# 의존성 전처리
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    deps[A].add(B)  # graph[A]: A학생 때문에 의존성 걸리는 학생들
    inDegree[B] += 1

# 진입차수가 0인 학생(=종속적이지 않은 학생)들을 큐에 모두 삽입
for studentNum in range(1, N+1):
    if (inDegree[studentNum] == 0):
        q.append(studentNum)

# 큐에서 하나씩 pop() 하며 줄 세움
while (q):
    studentNum = q.popleft()
    answer.append(str(studentNum))

    # studentNum 번 학생에 종속적이였던 학생들에 대하여
    for dep_studentNum in deps[studentNum]:
        inDegree[dep_studentNum] -= 1  # 각 학생들의 진입차수 감소
        if (inDegree[dep_studentNum] == 0):  # 종속성이 완전히 해제된 학생은 큐에 삽입
            q.append(dep_studentNum)


print(" ".join(answer))