from collections import deque

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

def check(place, r, c):
    q = deque([(r, c)])
    visited = [[False]*5 for _ in range(5)]
    visited[r][c] = True
    
    dist = 0
    while (q):
        for _ in range(len(q)):
            row, col = q.popleft()
            for i in range(4):
                nr, nc = row+dr[i], col+dc[i]
                if not (0 <= nr < 5 and 0 <= nc < 5):
                    continue
                if (visited[nr][nc]):
                    continue
                if (place[nr][nc] == 'X'):
                    continue
                if (place[nr][nc] == 'P'):
                    return False
                q.append((nr, nc))
            
        dist += 1
        if (dist >= 2):
            q.clear()
    return True
            
    


def solution(places):
    answer = []
    
    for place in places:
        pos = []
        for i in range(5):
            for j in range(5):
                if (place[i][j] == 'P'):
                    pos.append((i, j))
        
        test = []
        for r, c in pos:
            res = check(place, r, c)
            test.append(res)
        answer.append(int(all(test)))
    
    return answer