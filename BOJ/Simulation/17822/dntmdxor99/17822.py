read = lambda : map(int, input().split())
n, m, t = read()
num = [[0] * (n + 1)] + [list(read()) for _ in range(n)]        # 0번째 행은 어디가 첫 번째인지 확인하는 함수
temp = [[0] * m for _ in range(n + 1)]      # 인접하면서 같은 곳을 저장해놓음

for idx in range(1, t + 1):
    x, d, k = read()
    for i in range(x, n + 1, x):
        num[0][i - 1] = (num[0][i - 1] + (-1, 1)[d] * k) % m        # 방향을 돌림
    for i in range(1, n + 1):
        for j in range(m):
            if 0 != num[i][j] == num[i][val1 := (j + 1) % m]:
                temp[i][j] = temp[i][val1] = num[0][n] = idx        # 행에서 같은 애들
            if i != n and 0 != num[i][(val1 := (j + num[0][i - 1]) % m)] == num[i + 1][val2 := (j + num[0][i]) % m]:
                temp[i][val1] = temp[i + 1][val2] = num[0][n] = idx     # 열에서 같은 애들

    for i in range(1, n + 1):
        for j in range(m):
            if temp[i][j] == idx: num[i][j] = 0     # 인접하면서 같은 애들을 0으로 만듬

    if num[0][n] != idx:
        if s := sum([i.count(0) for i in temp[1:]]):        # Division by zero를 방지
            mean = sum([sum(i) for i in num[1:]]) / s       # 평균을 구함
        else:
            print(0)
            exit(0)
        for i in range(1, n + 1):
            for j in range(m):
                if val := num[i][j]:
                    num[i][j] = val + 1 if val < mean else val - 1 if val > mean else val

print(sum([sum(i) for i in num[1:]]))
