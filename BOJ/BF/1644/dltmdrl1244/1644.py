import sys
import math
input = sys.stdin.readline

n = int(input())
ans = 0
if n == 1:
    print(0)
    exit()

# 어떤 수가 소수인지 판별
def is_prime(a) :
    for i in range(2, int(math.sqrt(a)) + 1):
        if a != i and a % i == 0:
            return False
    return True

# 에라토스테네스의 체 기법으로 k 이하의 소수를 반환
def chae(k):
    a = [False, False] + [True] * (k-1)
    primes = []

    for i in range(2, k+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, k+1, i):
                a[j] = False
    return primes

# tail~head 까지의 부분합을 반환
def partsum(head, tail):
    return sprime[head] - sprime[tail - 1]

# 2,000,000 이하의 소수를 리스트로 만듦
primes = chae(2000000)

# 소수들의 부분합을 모두 계산
sprime = [primes[i] for i in range(len(primes))]
sprime.insert(0, 0)
for i in range(1, len(primes)+1):
    sprime[i] += sprime[i-1]

# 투포인터 알고리즘을 활용하여 n과 일치하는 부분합 정보가 있는지 배열 순회하며 확인
tail = 0
for head in range(len(primes)):
    while partsum(head, tail + 1) > n:
        tail += 1

    if partsum(head, tail + 1) == n:
        ans += 1

if n >= 2000000 and is_prime(n):
    ans += 1
print(ans)