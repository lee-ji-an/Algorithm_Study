import sys
input = sys.stdin.readline

n = int(input())
price = list(map(int, input().split()))
money = int(input())
result = []

# n이 1이면 적어도 하나의 숫자는 살 수 있다 했으므로 답은 무조건 0
if n > 1:
    minIdx_without0 = n - 1 - price[:0:-1].index(min(price[1:]))
else:
    print(0)
    exit()

minIdx_with0 = n - 1 - price[::-1].index(min(price))

# 0을 제외한 나머지 숫자 중 가장 싼 숫자를 먼저 맨 앞에 둔다
if money >= price[minIdx_without0]:
    result.append(minIdx_without0)
    money -= price[minIdx_without0]

# 0을 포함한 모든 숫자들 중 가장 싼 숫자를 가능한 한 붙인다
while money >= price[minIdx_with0]:
    if result and result[0] == 0:
        break
    result.append(minIdx_with0)
    money -= price[minIdx_with0]

# 앞에서부터 돈이 여유있는지 확인하고 더 큰 숫자로 교체할 수 있으면 교체한다
for idx, i in enumerate(result):
    for j in range(n-1, i-1, -1):
        if (idx == 0 and j == 0) or i == j:
            continue

        if money - price[j] + price[i] >= 0:
            result[idx] = j
            money -= price[j] - price[i]
            break

print(*result, sep="")