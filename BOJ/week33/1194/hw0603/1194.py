from collections import deque
import sys

# 샵이 벽, 점이 빈칸
# 0이 현재 위치, 1이 도착지
# abcdef -> 16진수 변환해서 비트마스킹

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, sys.stdin.readline().strip().split())
maze = [[None]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 초기 위치 잡고 미로 구축
for i in range(N):
    line = list(sys.stdin.readline().strip())
    for j, val in enumerate(line):
        maze[i][j] = val
        if (val == '0'):
            initPos = (i, j)

q = deque([(*initPos, 1)])  # (row, col, keychain)

# 현재 키체인으로 현재 칸의 문을 열 수 있는지 검사
def isOpened(doorType: str, keychain: int) -> bool:
    bitmask = 1 << (int(f"0x{doorType}", base=16))
    return bool(keychain & bitmask)

# 중복방문 여부 검증
def isAgain(row: int, col: int, keychain: int) -> bool:
    """
    1 1 1 0 -> hist
^   1 1 0 0 -> keychain
    -----------
    0 0 1 0 -> XOR 결과로 다른 비트만 켜짐. 이거랑 기존의 hist랑 OR 쳤을때, hist랑 달라지면 새 키가 존재하는 것
    """
    hist = visited[row][col]

    return hist == (hist | (hist ^ keychain))

# 키체인에 키 추가
def addKey(keychain: int, keyType: str) -> int:
    return (keychain | 1 << (int(f"0x{keyType}", base=16)))

moveCnt = 0
while (q):
    for _ in range(len(q)):
        row, col, keychain = q.popleft()

        for i in range(4):
            nr, nc, nkey = row+dr[i], col+dc[i], 0

            # 범위 밖 Skip
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            cur = maze[nr][nc]  # 현재 칸

            # 벽이면 Skip
            if (cur == '#'):
                continue
            # 문인데 열쇠가 없을 경우 Skip
            if ((doorType := cur).isupper() and not isOpened(doorType, keychain)):
                continue
            # 현재 가지고 있는 키체인으로 이미 방문했을 경우 Skip
            if (isAgain(nr, nc, keychain)):
                continue
            # 키인 경우 비트연산 해서 키체인에 추가
            if ((keyType := cur).islower()):
                nkey = addKey(keychain, keyType)
            # 도착 지점이면 탐색 종료
            if (cur == '1'):
                sys.exit(print(moveCnt+1))
            
            nkey = max(keychain, nkey)  # 키가 업데이트된 경우 원래 키보다 커질 것 (비트를 추가로 더 켰으므로)
            visited[nr][nc] = nkey  # 방문 내역에 현재 키체인 남김
            q.append((nr, nc, nkey))

    moveCnt += 1

print(-1)