import sys
input = sys.stdin.readline


def dfs(y, x):
    maps[y][x] = 'x'        ## 방문 처리, 어차피 위에 행에서 못가면 아래 행도 못감. 복원할 필요 없음

    if x == c - 2:
        return True

    if y > 0 and maps[y - 1][x + 1] != 'x':
        ## == '.' 보다 != 'x'가 300ms 가량 더 빠름
        if dfs(y - 1, x + 1):
            return True

    if maps[y][x + 1] != 'x':
        if dfs(y, x + 1):
            return True

    if y < r - 1 and maps[y + 1][x + 1] != 'x':
        if dfs(y + 1, x + 1):
            return True
    
    return False


if __name__ == "__main__":
    r, c = map(int, input().split())
    maps = [list(input().strip()) for _ in range(r)]

    ans = 0
    for i in range(r):
        if dfs(i, 0):
            ans += 1

    print(ans)