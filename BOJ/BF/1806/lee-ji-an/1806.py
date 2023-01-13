import sys
input = sys.stdin.readline
N, S = map(int, input().split())
A = list(map(int, input().split()))
total = A[0]
start, end, length, minLen = 0, 0, 1, float('inf')
while True:
    if total >= S:          # total이 S보다 크거나 같으면
        while True:         # start 포인터를 total이 S보다 작을 때까지 오른쪽으로 옮김
            if total < S:   # start > end 경우 있어도 ok
                break
            total -= A[start]
            start += 1
            length -= 1
        minLen = min(minLen, length+1)

    elif total < S:         # total이 S보다 작으면
        if end+1 == N:      # end를 뒤로 옮김
            break
        end += 1
        total += A[end]
        length += 1
if minLen == float('inf'):
    print(0)
else:
    print(minLen)