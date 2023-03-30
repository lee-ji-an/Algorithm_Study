import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol():
    n, m = map(int, input().split())
    maps = [0] + list(map(int, input().split()))

    good_stamp = [0] * (n + 1)

    for _ in range(m):
        i, w = map(int, input().split())
        good_stamp[i] += w      # 자신의 칭찬 스티커를 추가함

    print('0 ')
    for i in range(2, n + 1):
        good_stamp[i] += good_stamp[maps[i]]        # 직속 상사의 칭찬 스티커에 자신의 칭찬 스티커를 더함
        print("%d " % good_stamp[i])


sol()