import sys

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
visiable_cnt = [0] * N  # 각 빌딩에서 볼 수 있는 탑의 개수
nearest = [sys.maxsize] * N  # 볼 수 있는 탑들 중 가장 가까운 탑의 인덱스


# 왼쪽 -> 오른쪽, 오른쪽 -> 왼쪽으로 탐색하면서 현재 탑보다 높은 탑들의 index를 스택에 저장
# for iterator in (range(N), range(N-1, -1, -1)):
for iterator in (enumerate(towers), ((N-(i+1), val) for i, val in enumerate(reversed(towers)))):
    stack = []

    # for i in iterator:
    #     height = towers[i]
    for i, height in iterator:
        # 스택의 원소들 중 현재 탑의 높이보다 낮거나 같은(볼 수 없는) 원소는 모두 제거
        while (stack and towers[stack[-1]] <= height):
            stack.pop()

        if (stack_len := len(stack)):
            # 볼 수 없는 탑 제거 후 스택 원소의 개수는 i번째 탑에서 볼 수 있는 탑 개수
            visiable_cnt[i] += stack_len

            # 최근접 탑 갱신
            if (abs(stack[-1]-i) < abs(nearest[i]-i)):
                nearest[i] = stack[-1]

        stack.append(i)

# 정답 출력
for i in range(N):
    print(f"{visiable_cnt[i]} {nearest[i]+1}" if visiable_cnt[i] else 0)  # 문제에서 idx는 1부터 시작
