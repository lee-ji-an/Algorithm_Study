import math


def solution(m, n, startX, startY, balls):
    def dist(x1, y1, x2, y2):
        result = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
        return result

    def sol(startX, startY, endX, endY, m, n):
        up, down, left, right = float('inf'), float('inf'), float('inf'), float('inf')
        if not (startX == endX and startY < endY):
            up = dist(startX, 2 * n - startY, endX, endY)
            
        if not (startY == endY and startX < endX):
            right = dist(2 * m - startX, startY, endX, endY)
            
        if not (startX == endX and startY > endY):
            down = dist(startX, -startY, endX, endY)
            
        if not (startY == endY and startX > endX):
            left = dist(-startX, startY, endX, endY)
              
        return round(math.pow(min(up, down, left, right), 2))
    
    answer=[sol(startX, startY, endX, endY, m, n) for endX, endY in balls]
    
    return answer