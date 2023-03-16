import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

num_list = [0] * N

for i in range(N):
    num_list[i] = int(input())


def recur(prev_max, start, end):  # 바로 전 범위의 최댓값, 시작 인덱스, 끝 인덱스
    if start == end:
        return prev_max - num_list[start]
    elif start > end:
        return 0

    max_value = 0
    for i in range(start, end + 1):  # start ~ end 인덱스 사이의 최댓값과 최댓값의 인덱스를 구함
        if max_value < num_list[i]:
            max_idx = i
            max_value = num_list[i]

    left = recur(max_value, start, max_idx - 1)
    right = recur(max_value, max_idx + 1, end)

    return (prev_max - max_value) + left + right


print(recur(max(num_list), 0, N - 1))
