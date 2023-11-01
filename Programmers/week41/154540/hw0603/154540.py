from collections import deque

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    answer = []
    visited = [[False]*M for _ in range(N)]

    def bfs(row, col):
        life = int(maps[row][col])
        visited[row][col] = True

        q = deque([(row, col)])
        while (q):
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                if (maps[nr][nc] == 'X'):
                    continue
                if (visited[nr][nc]):
                    continue

                visited[nr][nc] = True
                life += int(maps[nr][nc])
                q.append((nr, nc))

        return life

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if (visited[i][j]):
                continue
            if (maps[i][j] == 'X'):
                continue
            answer.append(bfs(i, j))

    return sorted(answer) if answer else [-1]
