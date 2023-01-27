import sys
from collections import deque
input = sys.stdin.readline

def chae(k):
    primes = []
    check = [True] * (k+1)
    for i in range(2, k+1):
        if check[i]:
            primes.append(i)
            for j in range(2*i, k+1, i):
                check[j] = False

    return primes

# 에라토스테네스의 체를 활용하여 10000 이하의 소수를 미리 구해놓음
primes = set(chae(10000))

n = int(input())
for _ in range(n):
    n1, n2 = map(int, input().split())
    visited = [False] * (10001)
    visited[n1] = True
    found = False
    q = deque()
    q.append((n1, 0))

    while q:
        a, cnt = q.popleft()
        if a == n2:
            print(cnt)
            found = True
            break

        for i in range(4):
            for j in range(10):
                lista = list(str(a))
                if i == 0 and j == 0:
                    continue

                if int(lista[i]) == j:
                    continue

                lista[i] = j
                newa = int("".join(map(str, lista)))

                # 방문하지 않은 소수를 발견했다면 큐에 삽입
                if newa in primes and not visited[newa]:
                    # print("push", newa)
                    visited[newa] = True
                    q.append((newa, cnt + 1))

    # 큐가 빌 때까지 n2를 만들지 못한다면 Impossible
    if not found:
        print("Impossible")