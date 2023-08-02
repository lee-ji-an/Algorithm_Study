import sys
import heapq
input = sys.stdin.readline


def updateCntMaps(cnt, y, x):
    # 직선으로 쭉 나아감
    for i in range(4):      # 4방향으로
        dirY, dirX = dir[i]
        curY, curX = y, x
        while True:     # 쭉 나아감
            nextY, nextX = curY + dirY, curX + dirX
            if 0 <= nextY < h and 0 <= nextX < w:
                match maps[nextY][nextX]:
                    case '.':       # 빈 칸
                        if cntMaps[nextY][nextX] > cnt or \
                        (cntMaps[nextY][nextX] == cnt and chkMaps[i % 2][nextY][nextX] == False):        # 만약 기존의 거울 개수보다 적거나 같게 사용한다면
                            cntMaps[nextY][nextX] = cnt
                            chkMaps[i % 2][nextY][nextX] = True        # 방문 표시
                            heapq.heappush(hq, (cnt, nextY, nextX))
                            curY, curX = nextY, nextX       # 한 쪽으로 쭉 나아가기 위해
                        else:
                            break
                    case '*':
                        break
                    case 'C':
                        print(cnt)
                        exit(0)
            else:
                break


if __name__ == "__main__":
    w, h = map(int, input().split())
    maps = [list(input().strip()) for _ in range(h)]
    cntMaps = [[sys.maxsize] * w for _ in range(h)]      # 거울의 개수 체크
    chkMaps = [[[False]  * w for _ in range(h)] for _ in range(2)]      # 방문 체크, [0]은 수직, [1]은 수평
    hq = []
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'C':
                heapq.heappush(hq, (-1, i, j))
                maps[i][j] = '*'        # 벽으로 만듬

                # 다익스트라 알고리즘
                while hq:
                    cnt, y, x = heapq.heappop(hq)
                    updateCntMaps(cnt + 1, y, x)        # 벽을 만난 것이므로 +1해서 넣어줌