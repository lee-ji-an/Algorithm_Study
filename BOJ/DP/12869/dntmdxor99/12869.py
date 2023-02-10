import itertools

n = int(input())
x = y = z = 0
if n == 1:      # n이 1이라면 x만
    x = int(input())
elif n == 2:        # n이 2라면 x, y만
    x, y = map(int, input().split())
else:
    x, y, z = map(int, input().split())

dp = {(0, 0, 0) : 0}        # list 대신 딕셔너리 씀
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            for d_x, d_y, d_z in itertools.permutations([9, 3, 1], 3):      # 순열
                dp[(i, j, k)] = min(dp.get((i, j, k), float('inf')), dp[(max(0, i - d_x), max(0, j - d_y), max(0, k - d_z))] + 1)
                # 기존에 있는 i, j, k보다 값과 데미지를 줬을 때의 값을 비교하여 작은 걸 선택함
print(dp[(x, y, z)])