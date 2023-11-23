from collections import deque

def solution(msg):
    answer = []
    
    data = {chr(64+k): k for k in range(1, 27)}
    q = deque(msg)
    while (q):
        w = q.popleft()
            
        while (q and w+q[0] in data):
            w += q.popleft()
        answer.append(data.get(w))
        
        if (q):
            data[w+q[0]] = len(data)+1
    
    return answer
