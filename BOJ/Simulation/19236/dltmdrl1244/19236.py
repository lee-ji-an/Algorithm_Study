import copy
import sys
input = sys.stdin.readline

n = 4
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
# pos : 각 칸에 몇 번 물고기가 있는지
# dir : 각 칸에 물고기가 바라보고 있는 방향
pos = [[0] * n for _ in range(4)]
dir = [[0] * n for _ in range(4)]
ans = 0

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        pos[i][j] = tmp[j*2]
        dir[i][j] = tmp[j*2+1] - 1
    
# y, x 위치에서 sdir 방향을 바라보고 있는 상어가 먹을 수 있는 물고기의 위치와 번호를 리턴
def shark_move(y, x, pos, sdir):
    res = []
    sy, sx = y, x
    for i in range(n):
        sy += dy[sdir]
        sx += dx[sdir]
        
        if 0 <= sy < n and 0 <= sx < n:
            if pos[sy][sx] > 0:
                res.append([sy, sx, pos[sy][sx]])
    
    return res

def dfs(pos, dir, y, x, sdir, atesum):
    global ans
    # 먹은 위치를 0으로 만듦
    pos[y][x] = 0
    
    # 물고기의 번호 순서대로 이동
    for fish in range(1, 17):
        flag = 0
        for i in range(n):
            for j in range(n):
                if pos[i][j] == fish:
                    for _ in range(8):
                        ny = i + dy[dir[i][j]]
                        nx = j + dx[dir[i][j]]
                        # 범위 안에 있고, 상어 칸이 아니면 swap
                        if 0 <= ny < n and 0 <= nx < n and (ny, nx) != (y, x):
                            pos[i][j], pos[ny][nx] = pos[ny][nx], pos[i][j]
                            dir[i][j], dir[ny][nx] = dir[ny][nx], dir[i][j]
                            flag = 1
                            break
                        # 상어 칸이거나 범위를 벗어나면 방향 전환
                        else:
                            dir[i][j] = (dir[i][j] + 1) % 8
                if flag:
                    break
            if flag:
                break
    
    # shark_move 함수를 통해 현재 상어의 위치와 방향에서 먹을 수 있는 물고기들의 리스트를 구함
    nxt_fishes = shark_move(y, x, pos, sdir)
    # 먹을 수 있는 물고기가 없다면 정답 갱신
    if not nxt_fishes:
        ans = max(ans, atesum)
    
    else:
        for nxt in nxt_fishes:
            # 있다면 그 물고기 위치로 이동 및 먹기(번호 값 추가) 하면서 다시 재귀 호출, 단 pos와 dir은 원본 유지를 위해 복사본을 넘김
            dfs(copy.deepcopy(pos), copy.deepcopy(dir), nxt[0], nxt[1], dir[nxt[0]][nxt[1]], atesum + nxt[2])


# 처음에는 [0, 0]에서 시작
dfs(pos, dir, 0, 0, dir[0][0], pos[0][0])
print(ans)