import sys
from collections import deque
input = sys.stdin.readline


def dp(n):
    get_by_basic_part.setdefault(n, dict())

    for part in need_part[n]:       # 필요한 부품을 가져옴
        if part in basic_part:      # 필요한 부품이 기본 부품이라면
            get_by_basic_part[n][part] = get_by_basic_part[n].get(part, 0) + need_part[n][part]     # 기본 부품 개수를 업데이트함
        else:       # 필요한 부품이 기본 부품이 아니라 중간 부품이라면
            if part not in get_by_basic_part:       # 만약 기본 부품으로 중간 부품을 구할 수 있는 공식이 없다면 
                get_by_basic_part[part] = dp(part)      # 공식을 구함
            for sub_part in get_by_basic_part[part]:        # 그리고 기본 부품들을 더함
                get_by_basic_part[n][sub_part] = get_by_basic_part[n].get(sub_part, 0) + need_part[n][part] * get_by_basic_part[part][sub_part]
                # 특정 기본 부품으로 n을 만들 수 있는 개수 = 특정 기본 부품으로 n을 만들 수 있는 기존 개수 + 중간 부품의 개수 * 중간 부품을 만드는 기본 부품의 개수

    return get_by_basic_part[n]


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    need_part = [dict() for _ in range(n + 1)]
    basic_part = set([*range(1, n + 1)])
    for _ in range(m):
        x, y, k = map(int, input().split())
        need_part[x][y] = k
        basic_part.discard(x)

    get_by_basic_part = dict()

    ans = sorted(dp(n).items())
    for item in ans:
        print(*item, sep=' ')