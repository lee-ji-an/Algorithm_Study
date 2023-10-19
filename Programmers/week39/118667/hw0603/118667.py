from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    totlength = len(queue1) + len(queue2)
    
    # 두 큐 합이 홀수이면 예외처리
    if ((sum(queue1) + sum(queue2)) & 1):
        return -1
    
    q1sum = sum(queue1)
    q2sum = sum(queue2)
    
    visited = set([(q1sum, q2sum)])
    
    loopCnt = 0
    while not (q1sum == q2sum):
        if (q1sum > q2sum):
            queue2.append(queue1.popleft())
            q1sum -= queue2[-1]
            q2sum += queue2[-1]
        else:
            queue1.append(queue2.popleft())
            q2sum -= queue1[-1]
            q1sum += queue1[-1]
        loopCnt += 1
        
        if (loopCnt > totlength*2):
            loopCnt = -1
            break
    
    answer = loopCnt
    return answer
