import heapq

def solution(n, k, enemy):
    # 무적권의 개수가 충분히 많다면 모든 적을 다 막을 수 있음
    if (k >= len(enemy)):
        return len(enemy)
    
    heap = []  # 최대 힙
    answer = 0
    
    for round, e in enumerate(enemy):
        n -= e
        heapq.heappush(heap, -e)  # 막은 적들의 수를 최대 힙에 유지
        if (n < 0):
            if (k):  # 무적권 있으면 부활 시도
                k -= 1  # 사용
                n += -heapq.heappop(heap)  # 병사 회복
            else:
                answer = round
                break
    else:  # for~else
        answer = len(enemy)  # 모든 적을 다 막았을 경우
        
    return answer
