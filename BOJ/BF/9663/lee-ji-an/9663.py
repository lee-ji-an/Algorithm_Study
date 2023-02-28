import sys
input = sys.stdin.readline

N = int(input())

col_visited = [False] * N
board = [[False] * N for _ in range(N)]
d1 = [False] * (N * 2 - 1)    # /
d2 = [False] * (N * 2 - 1)    # \
ans = 0


def dfs(y):
    global ans
    if y == N - 1:
        ans += 1
        return

    for c in range(N):
        if not col_visited[c] and not d1[y + 1 + c] and not d2[y + 1 - c]:
            col_visited[c] = d1[y + 1 + c] = d2[(y + 1) - c] = True
            dfs(y + 1)
            col_visited[c] = d1[y + 1 + c] = d2[(y + 1) - c] = False


for i in range(N // 2):
    col_visited[i] = d1[i] = d2[-i] = True
    dfs(0)
    col_visited[i] = d1[i] = d2[-i] = False
ans *= 2
col = N // 2

if N % 2:
    col_visited[col] = d1[col] = d2[-col] = True
    dfs(0)
    col_visited[col] = d1[col] = d2[-col] = False

print(ans)
