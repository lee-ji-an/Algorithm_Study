import heapq
import sys

N = int(sys.stdin.readline())

for _ in range(N):  # 테케 순회
    minHeap, maxHeap = [], []
    k = int(sys.stdin.readline())
    isActive = [False] * k

    for id in range(k):  # k개의 인스트럭션 입력받음
        opcode, param = sys.stdin.readline().split()
        param = int(param)
        match (opcode):
            case 'I':
                heapq.heappush(minHeap, (param, id))  # min Heap에 삽입. (값, id)
                heapq.heappush(maxHeap, (-param, id))  # 같은 정보를 max Heap에도 삽입: 동기화는 id로 함
                isActive[id] = True
            case 'D':
                heap = maxHeap if param == 1 else minHeap  # param에 따라 조작할 heap 종류 설정
                while (heap and not isActive[heap[0][1]]):
                    heapq.heappop(heap)  # active한 노드가 나올 때 까지 계속 pop
                if (heap):
                    isActive[heap[0][1]] = False  # 첫 번째 만나는 active한 노드를 비활성화(삭제처리))
                    heapq.heappop(heap)  # 실제로 pop
    
    # 각 힙에서 비활성화 된 노드들을 전부 pop
    while (minHeap and not isActive[minHeap[0][1]]):
        heapq.heappop(minHeap)
    while (maxHeap and not isActive[maxHeap[0][1]]):
        heapq.heappop(maxHeap)
    
    # 결과 출력
    print(f"{-maxHeap[0][0]} {minHeap[0][0]}" if maxHeap and minHeap else 'EMPTY')

