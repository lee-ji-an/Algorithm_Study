import heapq
import sys

N, M, fuel = map(int, sys.stdin.readline().split())
matrix = [[0]*(N+1)]
for _ in range(N):
    tmp = [0] + list(map(int, sys.stdin.readline().split()))
    matrix.append(tmp)

# 문제에서 주어진 거리가 같은 승객의 우선순위에 따라
# 상 -> 좌 -> 우 -> 하 순으로 탐색
delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 상, 좌, 우, 하


# 승객의 위치 정보
guests = [(-1, -1, -1, -1)]  # (시작 좌표, 목적지 좌표)

taxi_row, taxi_col = map(int, sys.stdin.readline().split())  # 택시의 위치
for i in range(1, M + 1):
    src_row, src_col, dst_row, dst_col = map(int, sys.stdin.readline().split())
    matrix[src_row][src_col] = -i  # 맵에 승객의 번호를 저장
    guests.append((src_row, src_col, dst_row, dst_col))


# (row, col) 범위 체크
def inRange(x, y):
    return 0 < x <= N and 0 < y <= N


# 택시에서 가장 가까이 있는 승객을 찾음
def findNearest():
    q = []
    heapq.heappush(q, (0, taxi_row, taxi_col))  # (이동 거리, 택시 행, 택시 열)
    visited = [[False]*(N+1) for _ in range(N + 1)]
    visited[taxi_row][taxi_col] = True

    while (q):
        dist, row, col = heapq.heappop(q)

        if (matrix[row][col] < 0):  # 승객을 찾으면
            return -matrix[row][col], dist  # 승객의 인덱스와 이동 거리 반환

        for dr, dc in delta:
            nr, nc = row+dr, col+dc

            if not (inRange(nr, nc)):  # 범위밖 Skip
                continue
            if (visited[nr][nc] or matrix[nr][nc] == 1):  # 이미 방문했거나 벽이라면 Skip
                continue

            visited[nr][nc] = True
            heapq.heappush(q, (dist + 1, nr, nc))

    return (None, None)  # 태울 수 있는 승객을 찾지 못한 경우


# 승객을 태우고 목적지로 이동
def moveTo(dst_row, dst_col) -> bool:
    global fuel
    
    q = []
    heapq.heappush(q, (0, taxi_row, taxi_col))  # (이동 거리, 택시 행, 택시 열)
    visited = [[False]*(N+1) for _ in range(N+1)]
    visited[taxi_row][taxi_col] = True

    while (q):
        dist, row, col = heapq.heappop(q)

        if ((row, col) == (dst_row, dst_col)):
            if (fuel < dist):  # 목적지에 도달했으나 이동 거리가 더 길어 연료가 음수가 될 경우
                return False

            fuel += dist  # 이동 후 연료 보충
            return True

        for dr, dc in delta:
            nr, nc = row+dr, col+dc

            if not inRange(nr, nc):
                continue
            if visited[nr][nc] or matrix[nr][nc] == 1:
                continue

            visited[nr][nc] = True
            heapq.heappush(q, (dist+1, nr, nc))


# 아래 과정을 모든 손님이 목적지에 도착할 때 까지 총 M번 반복.
# 1) 태울 수 있는 승객을 찾음
# 2) 승객을 태우고 목적지로 이동
for _ in range(M):
    # 1. 태울 수 있는 승객을 찾음
    guestIdx, dist = findNearest()
    if (guestIdx is None):  # 태울 수 있는 승객이 없을 경우 -1 출력 후 종료
        sys.exit(print(-1))
    src_row, src_col, dst_row, dst_col = guests[guestIdx]

    # 2-1. 승객을 태움
    taxi_row, taxi_col = src_row, src_col  # 택시가 승객 위치로 이동
    fuel -= dist  # 승객 위치까지 이동하는데 연료 소모

    # 2-2. 목적지로 이동
    if not moveTo(dst_row, dst_col):  # False인 경우 승객을 목적지까지 태워줄 수 없음
        sys.exit(print(-1))
    taxi_row, taxi_col = dst_row, dst_col  # 택시가 승객의 목적지로 이동
    matrix[src_row][src_col] = 0  # 운행 완료한 승객의 정보 삭제

print(fuel)
