import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maps = list()
    for _ in range(n):
        heapq.heappush(maps, int(input()))      # 작은 애들끼리 더하는게 맞음

    """
    i, j, k >>> i < j < k
    i + j + (i + j + k) = 2 * (i + j) + k
    """

    ans = 0
    while len(maps) > 1:
        x = heapq.heappop(maps)
        y = heapq.heappop(maps)
        ans += x + y

        heapq.heappush(maps, x + y)
        
    print(ans)