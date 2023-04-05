import sys
input = sys.stdin.readline

n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]

tasks.sort(key = lambda x:(x[1]))

time = 0
ans = float('inf')
for duration, deadline in tasks:
    time += duration
    ans = min(ans, deadline - time)
    if time > deadline:
        print(-1)
        exit()

print(ans)