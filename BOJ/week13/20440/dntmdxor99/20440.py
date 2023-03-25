import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    maps = defaultdict(int)
    for _ in range(n):
        e, x = map(int, input().split())
        maps[e] += 1
        maps[x] -= 1

    max_value = 0
    cur_value = 0
    bef_value = 0
    start, end = -1, -1
    flag = False

    for i in sorted(maps.keys()):
        bef_value = cur_value       # 이전 값을 저장
        cur_value += maps[i]        # 현재 값을 갱신
        if cur_value > max_value:       # 만약 현재의 값이 최댓값보다 크다면 갱신
            max_value = cur_value
            start = i
            flag = True     # 중복으로 end를 갱신하는 것을 방지하기 위함
        if flag and bef_value == max_value and cur_value < max_value:
            # 위에서 갱신했을 때만 end를 갱신함
            # 이때 현재 값은 작으면서, 이전 값은 커야함
            end = i
            flag = False

    print(max_value)
    print(start, end)
