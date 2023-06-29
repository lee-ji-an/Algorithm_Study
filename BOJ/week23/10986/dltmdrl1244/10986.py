import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

t = 0
ans = 0
# k로 나누어 떨어지는 t를 처음 만났을 때 바로 +1 할 수 있도록 미리 0에는 1을 넣어놓음
count = {0: 1}

for i in range(n):
    t += arr[i]

    if t % k in count:
        ans += count[t % k]
        count[t % k] += 1
    else:
        count[t % k] = 1

print(ans)