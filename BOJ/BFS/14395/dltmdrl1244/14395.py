from collections import deque

s, t = map(int, input().split())
if s == t:
    print(0)
    exit(0)

q = deque()
q.append((s, []))
# 10**9 개에 해당하는 visited를 모두 저장할 수 없으므로 set에 저장
visited = set()
visited.add(s)

while q:
    c, hist = q.popleft()
    if c == t:
        print(*hist, sep="")
        exit(0)

    # set에 없으면, 즉 아직 탐색하지 않은 숫자라면 set 및 큐에 삽입
    if 1 <= c*c <= 10**9 and c*c not in visited:
        visited.add(c*c)
        q.append((c*c, hist + ['*']))

    if 1 <= c+c <= 10**9 and c+c not in visited:
        visited.add(c+c)
        q.append((c+c, hist + ['+']))

    # 빼기 연산은 무조건 결과가 0이 되고, 이후 더하기/곱하기/빼기 어떤 걸 해도 0에서 벗어나지 못하므로 고려 안 해줘도 된다.

    # 나누기 연산은 무조건 결과가 1이 되므로 그냥 1을 넣어줌.
    if c != 0 and 1 not in visited:
        visited.add(1)
        q.append((1, hist + ['/']))

print(-1)