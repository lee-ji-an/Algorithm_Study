import sys
input = sys.stdin.readline
import heapq


if __name__ == "__main__":
    n, m = map(int, input().split())
    subSequenceList = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    hp = []

    for _ in range(m):
        a, b = map(int, input().split())
        subSequenceList[a].append(b)        # 내 자식을 넣음
        degree[b] += 1      # 자식이 앞서서 몇 개의 문제를 풀어야 하는지

    for i in range(1, n + 1):
        if degree[i] == 0:      # 부모가 없는 문제
            heapq.heappush(hp, i)

    while hp:
        prior = heapq.heappop(hp)
        print(prior, end=' ')
        for sub in subSequenceList[prior]:      # 자식들의 단계를 한 단계 낮춤
            degree[sub] -= 1
            if degree[sub] == 0:
                heapq.heappush(hp, sub)     # 이제 부모가 없음 -> 출력해도 됨