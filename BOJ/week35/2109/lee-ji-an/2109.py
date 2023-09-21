import sys
import heapq
input = sys.stdin.readline

N = int(input())
lecture = []
hq = []
for i in range(N):
    p, d = map(int, input().split())
    lecture.append((d, p))

# 강연의 마감일 순서로 정렬 : (마감일, 돈)
lecture.sort()

# 최대한 1일부터 강연을 꽉꽉 채움
day = 0
money = 0
for i in range(N):
    period, price = lecture[i][0], lecture[i][1]

    # 강연이 마감일까지 다 차 있는 경우
    if period <= day:
        # 잡혀있는 강연 중 최소 강연료와 현재 강연료를 비교
        if price <= hq[0][0]:
            continue
        # 현재 강연의 강연료가 더 비싸다면 대체
        prev_price, idx = heapq.heappop(hq)
        heapq.heappush(hq, (price, idx))
    # 마감일 전에 비어있는 날이 있는 경우
    else:
        heapq.heappush(hq, (price, day))
        day += 1

print(sum(p for p, idx in hq))
