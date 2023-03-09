import sys
input = sys.stdin.readline

n = int(input())
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]
score = 0

def move_hori(blocks, t):
    pos = 0
    if t == 2: # 가로 블럭을 파란색부분에
        row = blocks[1][0]
        
        while pos != 5 and blue[row][pos+1] == 0:
            pos += 1
        
        blue[row][pos] = 1
        blue[row][pos-1] = 1
    
    elif t == 3: # 세로 블럭을 초록색부분에
        col = blocks[1][1]
        while pos != 5 and green[pos+1][col] == 0:
            pos += 1
        
        green[pos][col] = 1
        green[pos-1][col] = 1

    
def move_vert(blocks, t):
    pos = 0
    if t == 3 or t == 1: # 세로 블럭 or 1개짜리를 파란색부분에
        rows = []
        for block in blocks:
            rows.append(block[0])
        
        for i in range(5):
            flag = 0
            for row in rows:
                if blue[row][pos+1] == 1:
                    flag = 1
            if not flag:
                pos += 1
            else:
                break
        for row in rows:
            blue[row][pos] = 1
    
    pos = 0
    if t == 2 or t == 1: # 가로 블럭 or 1개짜리를 초록색부분에
        cols = []
        for block in blocks:
            cols.append(block[1])
        for i in range(5):
            flag = 0
            for col in cols:
                if green[pos+1][col] == 1:
                    flag = 1
            
            if not flag:
                pos += 1
            else:
                break
                
        for col in cols:
            green[pos][col] = 1
    
        
def check_score_delete():
    global score, green, blue
    
    # blue 행/열 반전
    t = []
    for item in list(zip(*blue)):
        t.append(list(item))
    blue = t
    
    # 채워진 줄 처리
    for i in range(2, 6):
        if sum(blue[i]) == 4:
            blue.pop(i)
            blue.insert(0, [0 for _ in range(4)])
            score += 1
        
        if sum(green[i]) == 4:
            green.pop(i)
            green.insert(0, [0 for _ in range(4)])
            score += 1
    
    # 넘친 줄 처리
    for i in range(2):
        if sum(blue[i]) >= 1:
            blue.pop()
            blue.insert(0, [0 for _ in range(4)])
        
        if sum(green[i]) >= 1:
            green.pop()
            green.insert(0, [0 for _ in range(4)])
    
    t = []
    for item in list(zip(*blue)):
        t.append(list(item))
    blue = t


for _ in range(n):
    t, y, x = map(int, input().split())
    tmp = [[y, x]]
    if t == 2:
        tmp.append([y, x+1])
    elif t == 3:
        tmp.append([y+1, x])
        
    # 이동
    move_vert(tmp, t)
    move_hori(tmp, t)
    # 채워진 줄 삭제 and 넘친 줄 처리
    check_score_delete()
    

cnt = 0
for i in range(4):
    cnt += sum(blue[i])
for i in range(6):
    cnt += sum(green[i])

print(score, cnt, sep="\n")