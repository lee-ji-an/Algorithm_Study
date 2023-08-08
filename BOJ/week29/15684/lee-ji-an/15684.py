import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[False] * N for _ in range(H)]
for m in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = True


# 현재 사다리가 조건에 맞는지 확인하는 함수
def simulation():
    for n in range(N):
        cur = n
        for h in range(H):
            if ladder[h][cur]:
                cur += 1
            elif cur - 1 >= 0 and ladder[h][cur - 1]:
                cur -= 1
        if n != cur:
            return False

    return True


def dfs(n, cnt):
    global ans
    if simulation():  # 문제의 조건을 만족한 경우 ans 갱신
        ans = min(ans, cnt)
        return
    if cnt >= 3 or cnt + 1 >= ans:
        return

    for i in range(n, (N - 1) * H):
        row, col = i % H, i // H

        # 현재 위치, 왼쪽, 오른쪽에 가로 선이 있는지 검사
        if ladder[row][col] or (col - 1 >= 0 and ladder[row][col - 1]) or (col + 1 < N and ladder[row][col + 1]):
            continue
        ladder[row][col] = True
        dfs(i + 1, cnt + 1)
        ladder[row][col] = False


ans = float('inf')
if M == 0:
    print(0)
else:
    dfs(0, 0)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
