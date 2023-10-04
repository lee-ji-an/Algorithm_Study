import sys
input = sys.stdin.readline


def sol():
    dist = [sys.maxsize] * (n+1)
    for i in range(n):      # 싸이클을 체크하기 위해 n번 실행
        for edge in edges:
            start, end, cost = edge

            if dist[end] > cost + dist[start]:      # 갱신됨
                dist[end] = cost + dist[start]
                if i == n - 1:      # n번째도 갱신되면 싸이클이 존재
                    return True

    return False


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, m, w = map(int, input().split())
        edges = []

        for _ in range(m):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))

        for _ in range(w):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))

        print("YES" if sol() else "NO")