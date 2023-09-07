import sys
input = sys.stdin.readline

def dfs(start, xIdx):
    # 끝까지 도달하면 return True
    if xIdx == m-1:
        return True
    
    for d in [-1, 0, 1]:
        if 0 <= start + d < n and board[start + d][xIdx + 1] != 'x':
            # 방문처리 해주고 dfs 재귀
            board[start + d][xIdx + 1] = 'x'
            if dfs(start + d, xIdx + 1):
                return True
    return False


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
ans = 0

for i in range(n):
    if dfs(i, 0):
        ans += 1
print(ans)
