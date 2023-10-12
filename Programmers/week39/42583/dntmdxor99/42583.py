from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    dq = deque([0] * bridge_length)
    onBriW = 0
        
    for i in truck_weights:     # 트럭이 정해진 순대로 지나감.
        onBriW -= dq.popleft()      # 맨 앞에 있는 애는 나오고, 다리 위 무게는 줄어듦
        
        while (onBriW + i) > weight:        # 새로운 트럭이 올라갈 수 있는가?
            # 올라갈 수 없으면, 앞에 있는 애들을 빼고 0을 집어넣음.
            answer += 1
            dq.append(0)
            onBriW -= dq.popleft()
        
        dq.append(i)        # 새로운 트럭이 올라감
        onBriW += i     # 무게 추가
        answer += 1     # 트럭 올라가는 시간 추가
    
    return answer + bridge_length