import sys

input = sys.stdin.readline

papers = [5] * 6
board = []
visited = [[False] * 10 for _ in range(10)]
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)


# 특정 좌표에 정사각형을 넣을 수 있는지 확인하는 함수
def check(row, col, size):
    for r in range(row, row + size):
        for c in range(col, col + size):
            if not(0 <= r < 10) or not(0 <= c < 10) or board[r][c] == 0 or visited[r][c]:
                return False

    return True


def dfs(loc, cnt):
    global ans

    for l in range(loc, 10 * 10):
        row, col = l // 10, l % 10
        if board[row][col] == 0 or visited[row][col]:
            continue

        # ptr : 붙일 수 있는 가장 큰 색종이 크기를 저장
        ptr = 0
        for i in range(5, 0, -1):
            if check(row, col, i):
                ptr = i
                break

        # 색종이 붙이기
        for i in range(ptr, 0, -1):
            if papers[i] > 0:

                papers[i] -= 1
                for r in range(row, row + i):
                    for c in range(col, col + i):
                        visited[r][c] = True

                dfs(l, cnt + 1)

                for r in range(row, row + i):
                    for c in range(col, col + i):
                        visited[r][c] = False
                papers[i] += 1
        break  # 비어 있는 칸은 존재할 수 없으므로 바로 종료해야 함.
    else:
        # 현재 위치 이후로 더 이상 색종이를 붙일 공간이 없을 때
        ans = min(cnt, ans)


ans = float('inf')
dfs(0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
