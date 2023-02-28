N, X = map(int, input().split())

burger = [1] * 51  # burger[i] = Level-i 버거의 총 재료 개수
patty = [1] * 51   # patty[i] = Levei-i 버거의 총 패티 개수

for i in range(1, N+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1  # B + f(N-1) + P + f(N-1) + B
    patty[i] = patty[i-1] + 1 + patty[i-1]


# Level-N 버거에서 X장을 먹었을 때, 먹은 패티의 개수
def eat(n, x):
    if (n == 0):  # 0-Level 버거는 패티 하나로 이루어져 있음
        return 1
    
    if (x == 1):  # 1개만 먹으면 무조건 햄버거번만 먹음
        return 0
    
    elif (x <= 1 + burger[n-1]):  # Case #1: 1 < X < 중간 패티
        return eat(n-1, x-1)  # N-1 레벨 버거에서 X-1장(맨 아래 번 하나 뺴고)을 먹는 경우와 같음
    
    elif (x == 1 + burger[n-1] + 1):  # Case #2: X = 중간 패티
        return patty[n-1] + 1  # N-1 레벨 버거의 패티 개수 + 1(중간 패티) 와 같음
    
    elif (x <= 1 + burger[n-1] + 1 + burger[n-1]):	# Case #3: 중간 패티 < X < 전체 재료
        return patty[n-1] + 1 + eat(n-1, x-(burger[n-1]+2))  # Case #2의 결과값 + (x-중간 패티까지의 재료 수(=중간 패티 이후로 더 먹을 수 있는 재료의 수))
    
    else:  # Case #4: 전체 재료를 다 먹는 경우
        return patty[n]  # N레벨 버거의 패티 개수와 같음

print(eat(N, X))
