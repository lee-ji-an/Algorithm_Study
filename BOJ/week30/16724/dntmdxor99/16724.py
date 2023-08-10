import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [list(input().strip()) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    ans = 0
    groupNum = 1

    dir = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}

    for y in range(n):
        for x in range(m):
            if visited[y][x] == 0:      # 방문한 적이 없어야 함
                curY, curX = y, x

                while True:     # DFS
                    visited[curY][curX] = groupNum      # 그룹 번호 부여

                    dirY, dirX = dir[maps[curY][curX]]      # 현재의 위치에 해당하는 방향을 받음
                    nextY, nextX = curY + dirY, curX + dirX     # 이동함

                    if visited[nextY][nextX] == 0:      # 방문한 적이 없다면 방문함
                        curY, curX = nextY, nextX
                    else:       # 만약 방문한 적이 있다면?
                        if visited[nextY][nextX] == groupNum:       # 근데 그게 싸이클이라면? +1하면 됨
                            ans += 1
                        break       # 만약 싸이클이 아니라, 다른 그룹에서 방문한 것이라면 이는 기존 그룹에 편입하는 것과 같다.

                groupNum += 1


    print(ans)