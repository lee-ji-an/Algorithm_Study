import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    subSequenceList = [[] for _ in range(n + 1)]        # 내 뒤에 오는 애들
    degree = [0] * (n + 1)      # 내 앞에 몇개 필요한지
    dq = deque()
    ans = []

    for _ in range(m):
        a, b = map(int, input().split())
        subSequenceList[a].append(b)
        degree[b] += 1

    for i in range(1, n + 1):
        if degree[i] == 0:
            dq.append(i)

    while dq:
        prior = dq.popleft()
        ans.append(prior)
        for sub in subSequenceList[prior]:
            degree[sub] -= 1
            if degree[sub] == 0:
                dq.append(sub)

    print(*ans, sep=' ')