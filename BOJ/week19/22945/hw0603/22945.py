import sys

N = int(sys.stdin.readline())
power = list(map(int, sys.stdin.readline().split()))

left, right = 0, N-1  # 초기 scope: 처음 ~ 끝
result = 0


# 구간 좁아지면: 개발자 수는 감소, 두 개발자의 능력치 최솟값은 증가'할 수도 있음'
while (left < right):
    # 현재 투포인터 위치에서 최댓값 갱신
    result = max(result, (right-left-1)*min(power[left], power[right]))

    # 왼쪽 개발자와 오른쪽 개발자 중 능력치가 낮은 포인터를 1칸 이동
    if (power[left] < power[right]):
        left += 1
    else:
        right -= 1

print(result)
