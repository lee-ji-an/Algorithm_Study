def solution(rows, columns, queries):
    answer = []
    
    maps = [[1] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            maps[row][column] += row * columns + column
    
    for query in queries:
        y1, x1, y2, x2 = map(lambda x : x - 1, query)
        temp = maps[y1][x1]
        minimum = temp
        
        # left
        for y in range(y1 + 1, y2 + 1):
            maps[y - 1][x1] = maps[y][x1]
            minimum = min(minimum, maps[y - 1][x1])
        
        # bottom
        for x in range(x1 + 1, x2 + 1):
            maps[y2][x - 1] = maps[y2][x]
            minimum = min(minimum, maps[y2][x - 1])
            
        # right
        for y in range(y2 - 1, y1 - 1, -1):
            maps[y + 1][x2] = maps[y][x2]
            minimum = min(minimum, maps[y + 1][x2])
            
        # top
        for x in range(x2 - 1, x1, -1):
            maps[y1][x + 1] = maps[y1][x]
            minimum = min(minimum, maps[y1][x + 1])
        
        maps[y1][x1 + 1] = temp
        
        answer.append(minimum)
    
    return answer