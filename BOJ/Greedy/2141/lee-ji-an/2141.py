import sys
input = sys.stdin.readline

N = int(input())

people_total = 0
part_sum = [0] * N
dist_list = []

for i in range(N):
    X, A = map(int, input().split())
    people_total += A
    dist_list.append((X, A))

dist_list = sorted(dist_list)  # 마을까지의 거리를 기준으로 정렬


def solve(dist_list, people_total):
    mid = people_total / 2
    people_cnt = 0
    for x, a in dist_list:
        people_cnt += a
        if people_cnt >= mid:  # 인구의 누적 합이 절반보다 커지는 시점에 해당 마을의 위치를 return
            return x


print(solve(dist_list, people_total))
