from collections import deque

def solution(places):
    def bfs(y, x, place):
        dq = deque()
        dq.append((y, x, 0))
        check[y][x] = True
        
        while dq:
            y, x, dist = dq.popleft()
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < 5 and 0 <= nx < 5:
                    if check[ny][nx] == False:
                        if place[ny][nx] == 'O':
                            if dist == 0:       # 한 번만 넣으면 됨.
                                check[ny][nx] = True
                                dq.append((ny, nx, dist + 1))
                        elif place[ny][nx] == 'P':
                            return False
        return True
    
    
    answer = []
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for place in places:
        check = [[False] * 5 for _ in range(5)]
        flag = True
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':      # 사람이 있다면 bfs를 수행함.
                    if not bfs(y, x, place):
                        flag = False
                        break
            if flag == False:       # flag가 False라면 break
                break
        answer.append(1 if flag else 0)
        
    return answer