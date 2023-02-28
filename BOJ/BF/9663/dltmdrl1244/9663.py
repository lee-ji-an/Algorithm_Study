n = int(input())
visited = [[False] * n for _ in range(n)]
ans = 0

def dfs(idx, visited):
    global ans
    if idx == n:
        ans += 1
        return
    
    vi = [v[:] for v in visited]
    
    print("dfs", idx, visited)
    
    for i in range(n):
        if not vi[idx][i]:
            for j in range(n - idx):
                vi[idx + j][i] = True
                if i + j < n:
                    vi[idx + j][i + j] = True
                if 0 <= i - j:
                    vi[idx + j][i - j] = True
                    
                dfs(idx + 1, vi)

dfs(0, visited)
print(ans)