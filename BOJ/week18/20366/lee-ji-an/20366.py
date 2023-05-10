import sys
input = sys.stdin.readline

N = int(input())

height = list(map(int, input().split()))
snowman_height = []
min_diff = float('inf')

# 눈덩이를 2개 골라 만들 수 있는 모든 조합 구하기
for i in range(N):
    for j in range(i + 1, N):
        snowman_height.append((height[i] + height[j], i, j))

snowman_height.sort()

# 만들 수 있는 눈사람의 높이 차를 계산해서 최솟값 구하기
for i in range(len(snowman_height) - 1):
    if snowman_height[i + 1][0] - snowman_height[i][0] < min_diff:
        # 겹치는 눈덩이가 있는지 확인
        if not {snowman_height[i + 1][1], snowman_height[i + 1][2]} & {snowman_height[i][1], snowman_height[i][2]}:
            min_diff = snowman_height[i + 1][0] - snowman_height[i][0]

print(min_diff)
