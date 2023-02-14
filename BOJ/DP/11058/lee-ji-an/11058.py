import sys
input = sys.stdin.readline

N = int(input())


def solve(n):
    max_cnt = n
    split_cnt = 1
    while True:
        split_cnt += 1
        s = (n - split_cnt + 1) // split_cnt  # 몫
        r = (n - split_cnt + 1) % split_cnt   # 나머지
        value = pow(s + 1, r) * pow(s, split_cnt - r)
        if max_cnt >= value:
            break
        max_cnt = value

    return max_cnt


print(solve(N))
