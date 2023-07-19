import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
ans = 0

for i in range(N):
    house.append(int(input()))
house.sort()

start, end = 1, house[-1] - house[0]
while start <= end:
    mid = (start + end) // 2  # 기준점
    point = house[0]
    cnt = 1
    # mid를 기준으로 했을 때 설치 가능한 집이 몇 개 나오는지 검사
    for i in range(1, N):
        if house[i] - point >= mid:
            cnt += 1
            point = house[i]
    # C 보다 크거나 같으면 간격을 더 넓혀도 됨 -> start = mid + 1
    # C 보다 작으면 간격을 더 좁혀야 함 -> end = mid - 1
    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
