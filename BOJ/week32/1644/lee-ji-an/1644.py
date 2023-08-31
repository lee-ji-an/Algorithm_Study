import sys
import math
input = sys.stdin.readline

N = int(input())
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
prime = []


# N 까지의 소수를 모두 찾아 prime 에 담는 함수
def find_prime():
    for i in range(2, int(math.sqrt(N)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, N + 1, i):
            is_prime[j] = False

    for i in range(2, N + 1):
        if is_prime[i]:
            prime.append(i)


# 소수의 연속합이 N인 경우를 count 하는 함수
def find_cnt():
    start, end = 0, 0
    prefix_sum = 0
    cnt = 0
    while start <= end:
        if prefix_sum < N:
            # end 옮기기
            if end >= len(prime):
                break
            prefix_sum += prime[end]
            end += 1
        elif prefix_sum > N:
            # start 옮기기
            prefix_sum -= prime[start]
            start += 1
        else:
            cnt += 1
            # start, end 옮기기
            if end >= len(prime):
                break
            prefix_sum -= prime[start]
            start += 1
            prefix_sum += prime[end]
            end += 1

    return cnt


find_prime()
print(find_cnt())
