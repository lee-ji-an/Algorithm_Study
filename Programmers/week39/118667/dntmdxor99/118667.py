def solution(queue1, queue2):
    answer = 0
    
    queue = queue1 + queue2     # 하나의 리스트로 생각함. 중간에 포인터로 가림막을 넣어준다고 생각하면 편함
    
    left, right, sumL, sumR = 0, len(queue1), sum(queue1), sum(queue2)
    oriLeft, oriRight = left, right
    l = len(queue)
    
    if (sumL + sumR) % 2:
        return -1
    
    while (left) % l != (right) % l:        # Circle Queue처럼 생각하기, 만나면 해결이 불가능
        if sumL == sumR:
            return answer
        
        elif sumL < sumR:
            sumR -= queue[right]
            sumL += queue[right]
            right = (right + 1) % l
            
            if oriRight == right:       # 기존 포인터 위치로 돌아오면 특정 값들이 계속해서 반복된다고 볼 수 있음. -> -1 반환
                break
        
        elif sumL > sumR:
            sumL -= queue[left]
            sumR += queue[left]
            left = (left + 1) % l
            
            if oriLeft == left:
                break
            
        answer += 1
        
    return -1