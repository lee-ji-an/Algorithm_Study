import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    t = int(input())
    maps = list()
    for _ in range(t):
        n = int(input())
        maps.clear()
        for _ in range(n):
            maps.append((input().strip()))

        maps.sort()     # 사전 순서대로 정렬해줌

        for i in range(n - 1):
            cur = maps[i]
            nxt = maps[i + 1]
            if len(cur) < len(nxt):     # 뒤에 애가 더 길이가 길 때만 체크하면 됨
                if cur == nxt[:len(cur)]:
                    print("NO")
                    break
        else:
            print("YES")
            