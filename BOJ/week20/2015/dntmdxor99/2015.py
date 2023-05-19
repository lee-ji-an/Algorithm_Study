import sys
input = sys.stdin.readline


def bf():
    cnt = 0
    win = 1

    while win <= n:
        for i in range(n - win + 1):
            if k == sum(maps[i: i + win]):
                cnt += 1
        win += 1

    return cnt


def optim():
    sums = {0: 1}       # 4, 0\n 1 1 1 1인 경우 인덱스 0, 1, 2의 합으로도 될 수 있으므로 넣어야 함
    total = 0
    cnt = 0

    for i in maps:
        total += i
        cnt += sums.get(total - k, 0)       # 현재까지의 누적합 - k를 했을때 값이 있다면 누적합 - k의 갯수만큼 더하면 됨, 없으면 그냥 0
        sums[total] = sums.get(total, 0) + 1        # 0이 있을 수 있으므로, 같은 인덱스도 계속 업데이트 해줘야 함

    return cnt


if __name__ == "__main__":
    n, k = map(int, input().split())
    maps = list(map(int, input().split()))

    print(optim())



