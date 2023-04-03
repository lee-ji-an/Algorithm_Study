import heapq
import sys

N = int(sys.stdin.readline())
fromTo = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])  # 시작시간 빠른 순 정렬
pq = []

useCnt = [0] * N
computers = [i for i in range(N)]  # 남은 자리를 뽑기 위한 힙큐

comIdx = heapq.heappop(computers)
useCnt[comIdx] += 1
heapq.heappush(pq, (fromTo[0][1], comIdx))  # 힙큐에 첫 사용자의 (사용 종료시간, 사용 컴퓨터 번호) push

for i in range(1, N):
    if (fromTo[i][0] < pq[0][0]):  # i번째 사람의 이용 시작 시간이 현재 컴퓨터의 이용 종료시간보다 이르면
        comIdx = heapq.heappop(computers)
        useCnt[comIdx] += 1
        heapq.heappush(pq, (fromTo[i][1], comIdx))  # 새로운 컴퓨터 사용
    else:  # 컴퓨터를 추가하지 않고 빈 컴퓨터를 그대로 사용 가능할 때
        prev_end, prev_idx = heapq.heappop(pq)
        # 현재 시점에서 여러 컴퓨터가 사용 종료된 경우, 그 중에서 idx가 작은 컴퓨터를 골라야 함
        # -> 루프 안에서 사용 종료된 컴퓨터의 인덱스를 모두 빈 자리로 마킹
        # 1회 pop 했더니 pq top의 종료시간이 현재의 start 시간보다 늦은 경우
        # (즉, 한 컴퓨터만 자리가 난 경우) 루프로 진입하지 않음
        while (pq and pq[0][0] <= fromTo[i][0]):
            # 1회 pop 후에도 pq top의 종료시간이 현재의 start 시간보다 이른 경우
            heapq.heappush(computers, prev_idx)  # 빈 컴퓨터 리스트에 추가하고 continue
            prev_end, prev_idx = heapq.heappop(pq)  # 사용 종료된 컴퓨터를 pop

        # 빈 컴퓨터를 리스트에 추가하고 난 후 가장 작은 Idx 반환
        comIdx = heapq.heappushpop(computers, prev_idx)
        useCnt[comIdx] += 1
        heapq.heappush(pq, (fromTo[i][1], comIdx))


comCnt = N - useCnt.count(0)
print(comCnt)
print(*useCnt[:comCnt], sep=' ')
