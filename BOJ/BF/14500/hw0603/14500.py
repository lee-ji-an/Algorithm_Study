import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def dfs(r, c, idx, total):
    global answer

    # 가지치기: 앞으로 갈 수 있는 모든 블럭이 matrix의 maxValue일 때보다 answer(현재 내가 구한 최댓값)이 더 크면
    if (answer >= total + maxValue * (4 - idx)):
        return
    
    # 마지막 칸(4번째) 도달 시
    if (idx == 4):
        answer = max(answer, total)
        return
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not (0 <= nr < N and 0 <= nc < M and not visited[nr][nc]):
            continue  # 방문했거나 범위 밖 Skip
        if (idx == 2):  # T자형 블럭 처리: 2번째 블럭에서는 내가 갈 수 있는 곳을 살펴보지만, 자리이동 x
            visited[nr][nc] = True
            dfs(r, c, idx+1, total + matrix[nr][nc])
            visited[nr][nc] = False
        
        visited[nr][nc] = True
        dfs(nr, nc, idx+1, total + matrix[nr][nc])
        visited[nr][nc] = False


maxValue = max(map(max, matrix))
answer = 0
for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, 1, matrix[r][c])
        visited[r][c] = False

print(answer)
