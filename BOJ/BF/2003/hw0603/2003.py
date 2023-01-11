import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

count, subtotal = (0, 0)
start, end = (0, 0)

# 투 포인터 사용
for start in range(N):  # start 포인터는 기본적으로 계속 증가
    while (end < N):  # end 포인터가 끝까지 갈 때 까지 반복
        if (subtotal >= M):  # 현재 scope의 부분합이 M 이상이면 루프 탈출
            break
        subtotal += nums[end]  # end 포인터가 증가할 것이므로, scope를 오른쪽으로 한 칸 밀어줌
        end += 1
    if (subtotal == M):
        count += 1  # 부분합이 M과 같을 때 카운트 증가

    subtotal -= nums[start]  # start 포인터가 증가할 것이므로, scope를 오른쪽으로 한 칸 밀어줌

print(count)
