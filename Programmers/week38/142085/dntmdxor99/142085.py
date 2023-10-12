import heapq

def solution(n, k, enemy):
    answer = 0
    
    l = len(enemy)
    if k >= l:      # 모두 다 막을 수 있음
        return l
    
    hp = list()
    for i in range(k):      # k개까지는 일단 때려박음
        heapq.heappush(hp, enemy[i])
    
    while n >= 0 and (i := i + 1) < l:      # n이 0보다 크거나 같고, i에는 1을 계속 더함
        heapq.heappush(hp, enemy[i])        # 일단 새로 오는 적을 넣음
        n -= heapq.heappop(hp)      # k의 한도 내에서 가장 작은 애를 뺌. 그러면 hp 안에는 i 라운드까지 중에 가장 큰 적들이 들어가있음

    return i