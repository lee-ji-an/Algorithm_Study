import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
timelist = []
mogi = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    # 들어온것, 나간것 True, False 로 구분
    timelist.append([a, True])
    timelist.append([b, False])

timelist.sort(key = lambda x:(x[0]))

# 각 시간에 존재하는 모기 수 구하는 부분
cur_mogi = 0
for time, inout in timelist:
    if inout:
        cur_mogi += 1
    else:
        cur_mogi -= 1
    
    mogi[time] = cur_mogi

# 시간 순으로 정렬
mogi = dict(sorted(mogi.items()))


max_mogi = 0
cur_mogi = 0
flag = 0
# max_mogi : 가장 많은 모기 수
# cur_mogi : 현재 방 안에 있는 모기 수
# flag : 구간의 시작과 끝을 표시하기 위한 변수
for time, mogis in mogi.items():
    # max모기보다 많은 수의 모기가 있다면 그 지점이 정답구간의 시작
    if mogis > max_mogi:
        max_mogi = mogis
        in_answer = time
        # 구간 시작
        flag = 1
    
    # 구간이 진행되고 있었는데 모기가 max모기보다 적어졌다면 그 지점이 정답구간의 끝
    if mogis < max_mogi and flag:
        out_answer = time
        # 구간 끝 표시
        flag = 0
    
    cur_mogi = mogis

print(max_mogi)
print(in_answer, out_answer)