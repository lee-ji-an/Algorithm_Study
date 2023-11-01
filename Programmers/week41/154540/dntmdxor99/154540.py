from collections import deque

def solution(maps):
    def bfs(y, x):        
        food = int(maps[y][x])     # 무인도의 음식들
        dq = deque([(y, x)])
        check[y][x] = True
        
        while dq:
            y, x, = dq.popleft()
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w:
                    if maps[ny][nx] != 'X':
                        if not check[ny][nx]:
                            food += int(maps[ny][nx])
                            dq.append((ny, nx))
                            check[ny][nx] = True
        return food               
        
    answer = []
    
    h = len(maps)
    w = len(maps[0])
    check = [[False] * w for _ in range(h)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for y in range(h):
        for x in range(w):
            if maps[y][x] != 'X' and not check[y][x]:
                answer.append(bfs(y, x))        # 바다가 아니고, 방문한 적이 없으면 bfs 실행
    
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer