n = int(input())
queens = [-1 for _ in range(n)]
ans = 0


def check(row, n, q):
    if n in q:
        return False
    for i in range(row+1):
        if q[row-i] == n-i or q[row-i] == n+i:
            return False
    return True


def recur(idx, q):
    global ans
    if idx == n:
        ans += 1
        return
    
    for i in range(n):
        if check(idx, i, q):
            q[idx] = i
            recur(idx + 1, q)
            q[idx] = -1
        
recur(0, queens)
print(ans)