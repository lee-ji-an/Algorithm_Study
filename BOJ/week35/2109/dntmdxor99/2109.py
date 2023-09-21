import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maps = []
    go_to_this_day = dict()

    for _ in range(n):
        pay, day = map(int, input().split())
        go_to_this_day[day] = day
        heapq.heappush(maps, (-pay, day))

    check = set()       # 어느 날짜들을 넣었는지
    ans = 0
    capacity = 0        # 어느 날짜까지는 꽉 차있음

    while maps:
        pay, day = heapq.heappop(maps)
        day_ori = day       # 추후 원래 값을 이용해야 함
        day = go_to_this_day[day]     # 특정 날짜까지 갈 수 있는 강연은 이 날짜 아래로 갈 수 있음

        if day <= capacity: continue     # 특정 날짜까지 꽉 차있는데, 그것보다 작으면 못감

        while day > 0 and day in check:     # 날짜가 1보다 커야하고, 예약이 없어야 함, go_to_this_day에서 체크해도, 다른 날짜가 기한인 강의가 이미 예약했을 수도 있으므로
            day -= 1
        if day:     # 0이 아니면 예약
            check.add(day)
            ans -= pay
            go_to_this_day[day_ori] -= 1        # 특정 날짜까지 갈 수 있는 강연 날짜는 현재 값 - 1을 해야함
        else:
            capacity = day_ori      # 한계값
            go_to_this_day[day_ori] = 0     # 특정 날짜까지 할 수 있는 강의는 이제 없음

    print(ans)