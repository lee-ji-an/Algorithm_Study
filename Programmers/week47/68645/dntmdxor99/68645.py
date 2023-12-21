def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:      # 아래
                x += 1          
            elif i % 3 == 1:    # 오른쪽
                y += 1            
            elif i % 3 == 2:    # 위
                x -= 1
                y -= 1      
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j:
                answer.append(j)
    return answer