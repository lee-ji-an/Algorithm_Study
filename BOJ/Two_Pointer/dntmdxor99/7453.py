import sys
from collections import Counter
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a, b, c, d = [], [], [], []
    for _ in range(n):
        t1, t2, t3, t4 = map(int, input().split())
        a.append(t1)
        b.append(t2)
        c.append(t3)
        d.append(t4)

    ab, cd = [i + j for i in a for j in b], [i + j for i in c for j in d]

    cnt = 0
    cd = Counter(cd)
    for i in ab:
        cnt += cd[-i]
    print(cnt)
