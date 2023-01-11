import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [arr[i] for i in range(n)]
s.insert(0, 0)

ans = 0
tail = 1

def partsum(head, tail):
    return s[head] - s[tail - 1]

for i in range(1, n+1):
    s[i] += s[i-1]

for head in range(1, n+1):
    while partsum(head, tail) > m and tail < head:
        tail += 1

    if partsum(head, tail) == m:
        ans += 1

print(ans)