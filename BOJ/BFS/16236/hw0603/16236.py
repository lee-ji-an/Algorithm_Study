from collections import deque
import sys

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

N = int(sys.stdin.readline())
matrix = []
shark_pos = None
shark_size = 2
fish_cnt = 0


for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if (line[j] == 9):
            line[j] = 0  # 아기상어 위치를 별도로 저장한 후, 지도에서는 0으로 바꿔줌
            shark_pos = (i, j)
        elif (0 < line[j] <= 6):
            fish_cnt += 1
    matrix.append(line)


def bfs(row, col):
    q = deque([(row, col, 0)])  # row, col, dist
    visited = [[False]*N for _ in range(N)]
    visited[shark_pos[0]][shark_pos[1]] = True  # 초기 상어 위치 방문 처리

    candidate_list = []

    dist_min = sys.maxsize  # 무한대로 초기화
    while (q):
        row, col, dist = q.popleft()
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]

            if (0 <= n_row < N and 0 <= n_col < N):  # 새로운 좌표가 범위 내에 있고
                if not (visited[n_row][n_col]):  # 아직 방문하지 않았으며
                    if (matrix[n_row][n_col] <= shark_size):  # 그곳의 물고기 크기가 상어 크기 이하일때
                        visited[n_row][n_col] = True  # 방문 처리

                        if (0 < matrix[n_row][n_col] < shark_size):  # 물고기가 상어보다 더 작다면
                            dist_min = dist  # 밑에서 큐에 삽입할 때, (현재 dist)+1을 해도 dist_min 이하인 값들만 삽입하므로, 여기서 dist는 항상 현재의 dist_min 보다 작음. 최솟값 업데이트.
                            # dist_min 은 초기에 아주 큰 수였다가, 먹을 수 있는 물고기를 처음 만났을 때, 그 물고기까지의 거리로 업데이트됨.
                            # 그 이후로는 dist_min 값보다 작은 값들에 대해서만 큐에 삽입하며 조사하면 됨
                            
                            # (n_row, n_col)은 먹을 수 있는 물고기이므로 후보군 리스트에 추가. 큐에서 pop한 좌표와 한 칸 인접한 좌표이므로 거리는 dist+1.
                            # 문제 조건에서 거리, 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기 순으로 우선순위가 주어졌으므로
                            # 정렬을 염두에 두고 (dist+1, row, col) 순으로 튜플 생성하여 추가
                            candidate_list.append((dist+1, n_row, n_col))

                        if (dist+1 <= dist_min):  # 현재까지 구해진 거리의 최솟값 이하인 값(이동하여 조사해 볼 가치가 있는 값)들만 큐에 삽입
                            q.append((n_row, n_col, dist+1))

    # 큐가 빌 때 까지 반복 후 먹을 물고기를 찾았다면, 그 중 dist가 가장 작은 값 반환
    # dist_list 가 비었다면(=먹을 수 있는 물고기가 없으면) False 반환
    return sorted(candidate_list)[0] if candidate_list else False


# 남은 물고기가 없을 때 까지 반복
second = 0
eat_fish_cnt = 0
while (fish_cnt):
    result = bfs(*shark_pos)  # 현재 상어 위치에서 최선의 물고기 한 마리 먹고 난 후의 결과 받음
    if not (result):
        break

    dist, *shark_pos = result  # bfs 한 번 돌고 난 후 상어의 위치 업데이트
    second += dist  # 시간(이번 시행에서 한 마리 먹기 위해 움직인 거리) 증가
    fish_cnt -= 1  # 물고기 하나 먹었으니까 물고기 수 감소
    eat_fish_cnt += 1  # 마지막 성장 후 현재까지 먹은 물고기 수 증가

    # 자기 크기와 같은 개수의 물고기를 먹었다면 성장 시킨 후, 먹은 물고기 수 초기화
    if (eat_fish_cnt == shark_size):
        shark_size += 1
        eat_fish_cnt = 0
    matrix[shark_pos[0]][shark_pos[1]] = 0  # 상어의 새로운 위치에는 물고기가 이제 없음

print(second)
