import sys
input = sys.stdin.readline

def make_prime(n):
    primes = []
    is_prime = [False, False] + [True for _ in range(n-1)]

    for i in range(2, n+1):
        if not is_prime[i]:
            continue

        for j in range(2*i, n+1, i):
            is_prime[j] = False

        primes.append(i)

    return primes        


def partsum(i, j):
    return s[j] - s[i]


n = int(input())
primes = make_prime(n)
s = [0]
ans = 0


if n == 1:
    print(0)
    exit()

for i in range(len(primes)):
    s.append(s[-1] + primes[i])

# 두 포인터를 사용, right는 범위의 머리, left는 범위의 꼬리
# right를 한칸 전진 -> 구간합이 n보다 작거나 같을 때까지 left를 당기는 방식으로 탐색을 반복
left = 0
for right in range(len(primes) + 1):
    while partsum(left, right) > n:
        left += 1
    
    if partsum(left, right) == n:
        ans += 1

print(ans)