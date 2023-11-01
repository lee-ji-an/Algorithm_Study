def solution(m, n, startX, startY, balls):
    def calculate(a, b, c, d):
        x = a*(b-d)/(c+a)
        smallHypotenuse = (a**2+x**2)**0.5
        return round(
            (smallHypotenuse*2 + (smallHypotenuse*(c-a))/a) ** 2
        )
    
    answer = []
    
    for targetX, targetY in balls:
        # 축변환 상대좌표
        relativeCoords = [
            (startX, startY, targetX, targetY),
            (n-startY, startX, n-targetY, targetX),
            (m-startX, n-startY, m-targetX, n-targetY),
            (startY, m-startX, targetY, m-targetX)
        ]
        
        # 상대좌표 중 해당 방향으로 이동 시 벽보다 다른 공에 먼저 맞는 경우 제거
        for idx, (a, b, c, d) in enumerate(relativeCoords):
            if (a > c and b == d):
                relativeCoords.pop(idx)
                break
                
        answer.append(min(calculate(a, b, c, d) for a, b, c, d in relativeCoords))
    
    return answer
