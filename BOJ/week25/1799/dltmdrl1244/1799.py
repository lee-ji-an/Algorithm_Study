import sys
input = sys.stdin.readline

# 백트래킹
def recur(idx, visited):
    global ans
    flag = 0
    if idx == 2*n-1:
        return
    
    for i in range(idx + 1):
        if 0 <= i < n and 0 <= idx - i < n:
            if board[i][idx-i] and (idx - 2*i not in visited):
                flag = 1
                ans = max(ans, len(visited) + 1)
                visited.add(idx - 2*i)
                recur(idx + 1, visited)
                visited.remove(idx - 2*i)
    
    if not flag:
        recur(idx + 1, visited)
    

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
visited = set()

recur(0, visited)
print(ans)