import sys
import heapq
input = sys.stdin.readline


def dijkstra(maps):
    # 다익스트라 알고리즘을 사용
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    value = [[sys.maxsize] * n for _ in range(n)]
    heap = []
    heapq.heappush(heap, (0, 0, 0))

    while True:
        score, y, x = heapq.heappop(heap)
        if (y, x) == (n - 1, n - 1): break
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if value[ny][nx] > score + maps[ny][nx]:
                    value[ny][nx] = score + maps[ny][nx]
                    heapq.heappush(heap, (value[ny][nx], ny, nx))

    return value[n - 1][n - 1] // 10000     # 정답의 출력을 위해 10,000으로 나눈 몫을 반환하면 됨


def A_star(maps):
    # 에이스타 알고리즘?을 사용
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    value = [[sys.maxsize] * n for _ in range(n)]
    heap = []
    heapq.heappush(heap, (n * 2, 0, 0))

    while True:
        score, y, x = heapq.heappop(heap)
        score = score + (2 * n - y - x)
        if (y, x) == (n - 1, n - 1): break
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if value[ny][nx] > score + maps[ny][nx]:
                    value[ny][nx] = score + maps[ny][nx]
                    heapq.heappush(heap, (value[ny][nx] - (2 * n - ny - nx), ny, nx))

    return value[n - 1][n - 1] // 10000  # 정답의 출력을 위해 10,000으로 나눈 몫을 반환하면 됨


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(lambda x: 10000 if x == '0' else 0, input().strip())) for _ in range(n)]
    # 일요일 아침의 데이트와 비슷하게 벽이 있는 곳은 10000으로 설정하여 문제를 풀었음

    # print(dijkstra(maps))
    print(A_star(maps))
