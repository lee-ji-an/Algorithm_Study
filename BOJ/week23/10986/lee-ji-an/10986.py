import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = list(map(int, input().split()))

prefix_sum = 0
prefix_sum_dict = defaultdict(int)
cnt = 0

for i in range(N):
    # 현재 누적합의 M으로 나눈 나머지 구함
    prefix_sum = (prefix_sum + sequence[i]) % M

    # 정답에 해당되는 경우의 수를 세는 부분
    # 현재까지의 누적합이 M으로 나누어떨어지면 +1, 현재 누적합의 나머지와 같은 수를 dict에서 조회 그 수만큼 더함
    if prefix_sum == 0:
        cnt += 1
    if prefix_sum in prefix_sum_dict:
        cnt += prefix_sum_dict[prefix_sum]

    # dict 갱신
    prefix_sum_dict[prefix_sum] += 1
print(cnt)
