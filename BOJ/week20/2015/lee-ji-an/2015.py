import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, input().split()))

sum_list = [(0, 0)]
sum_dict = {}
sum_value = 0
ans = 0

for i in range(0, N):
    # sum_value 에 누적합을 저장
    sum_value += num_list[i]

    # i 위치를 끝지점으로 하는 정답이 있는지 확인하고 정답 횟수에 추가
    if sum_value - K in sum_dict:  # i 위치까지의 누적합이 sum_value 이므로 sum_value - K 가 존재하는지 확인
        ans += len(sum_dict[sum_value - K])

    # i 위치까지의 누적합을 sum_dict에 추가
    if sum_value in sum_dict:
        sum_dict[sum_value].append(i)
    else:
        sum_dict[sum_value] = [i]

# 0번째 인덱스부터 시작하는 경우의 수를 정답 횟수에 추가
if K in sum_dict:
    ans += len(sum_dict[K])

print(ans)
