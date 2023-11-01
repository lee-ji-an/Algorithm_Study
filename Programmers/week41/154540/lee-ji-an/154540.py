def solution(maps):
    from collections import deque
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]

    def bfs(row, col):
        day = 0

        q = deque()
        visited[row][col] = True
        q.append((row, col))
        day += int(maps[row][col])

        while q:
            r, c = q.popleft()
            for d in range(4):
                mv_r, mv_c = r + dr[d], c + dc[d]
                if not (0 <= mv_r < N) or not (0 <= mv_c < M):
                    continue
                if maps[mv_r][mv_c] == 'X' or visited[mv_r][mv_c]:
                    continue

                visited[mv_r][mv_c] = True
                q.append((mv_r, mv_c))
                day += int(maps[mv_r][mv_c])

        # 전체 식량의 합을 반환
        return day

    answer = []
    for r in range(N):
        for c in range(M):
            if maps[r][c] != 'X' and not visited[r][c]:
                # 방문처리가 안 된 섬을 발견하면 bfs 시작 -> 섬 찾기
                answer.append(bfs(r, c))

    # 섬이 없을 때
    if not answer:
        answer.append(-1)

    return sorted(answer)
