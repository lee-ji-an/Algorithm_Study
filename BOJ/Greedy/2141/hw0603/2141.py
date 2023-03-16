import sys

town = []
population = 0

N = int(sys.stdin.readline())
town = []
for i in range(N):
    idx, p = map(int, sys.stdin.readline().split())
    town.append((idx, p))
    population += p

town.sort()  # 마을 번호를 기준으로 정렬

cnt = 0
for idx, p in town:
    cnt += p
    if (cnt >= population/2):  # 현재 포인터까지의 인구가 전체 인구의 절반 이상이 되는 순간
        print(idx)
        break
