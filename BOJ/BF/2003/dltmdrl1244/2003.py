import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [arr[i] for i in range(n)]
s.insert(0, 0)

ans = 0
tail = 1

def partsum(head, tail): # head부터 tail까지의 합을 반환
    return s[head] - s[tail - 1]

for i in range(1, n+1): # s[i]에 1..i까지의 합을 저장
    s[i] += s[i-1]

for head in range(1, n+1):
    # 부분합이 구하고자 하는 m보다 크면 부분합을 줄이기 위해 tail을 1 증가
    while partsum(head, tail) > m and tail <= head:
        tail += 1

    if partsum(head, tail) == m:
        ans += 1

print(ans)