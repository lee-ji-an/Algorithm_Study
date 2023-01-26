from collections import deque
'''
f : 총 층수
s : 시작
g : 목적지
u : 위로 갈수있는 층수
d : 아래로 갈수있는 층수
'''
f, s, g, u, d = map(int, input().split())
q = deque()
q.append((s, 0))
visited = set()
visited.add(s)

while q:
    c, cnt = q.popleft()
    if c == g:
        print(cnt)
        exit(0)

    for i in (u, -d):
        nxt = c + i
        if 1 <= nxt <= f and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, cnt + 1))

print("use the stairs")