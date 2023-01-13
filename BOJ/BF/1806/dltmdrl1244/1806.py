import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [arr[i] for i in range(n)]
s.insert(0, 0)

min_len = float('inf')
tail = 1

def partsum(head, tail):
    return s[head] - s[tail - 1]

for i in range(1, n+1):
    s[i] += s[i-1]

for head in range(1, n+1):
    while tail <= head and partsum(head, tail) >= m:
        min_len = min(min_len, head - tail + 1)
        tail += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)