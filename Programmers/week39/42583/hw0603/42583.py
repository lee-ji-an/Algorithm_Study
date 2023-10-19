from collections import deque

def solution(bridge_length, weight_cut, trucks):
    answer = 0
    trucks = deque(trucks)
    bridge = deque([0]*bridge_length)
    weight = 0
    
    while (trucks):
        answer += 1  # 시간 증가
        weight -= bridge.popleft()
        
        if (weight+trucks[0] <= weight_cut):
            w = trucks.popleft()
            weight += w
            bridge.append(w)  # 트럭 올리기
        else:
            bridge.append(0)  # 빈칸 올리기
    
    
    return answer + len(bridge)