import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time_list = []

for i in range(N):
    time_list.append(int(input()))

ans = 0
start, end = 1, M * min(time_list)  # start에 최솟값, end에 최댓값 저장

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(N):  # 시간이 mid 일 때 심사 시뮬레이션
        cnt += mid // time_list[i]

    # 모두 심사 가능한지 확인 -> start, end 조정
    if cnt >= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
