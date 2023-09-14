from bisect import bisect_left
import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())

data = sorted((P[i], i) for i in range(N))  # (price, num)

# 자릿수를 먼저 확정지어놓고, 앞부터 한자리씩 순회하며 남은 예산 안에서 바꿔 나감

# 1. 첫 자리에 올 0이 아닌 가장 저렴한 숫자 구함
if (N == 1):
    sys.exit(print(0))
first_digit = data[0] if data[0][1] != 0 else data[1]

# 2. 첫 자리 구하고 남은 돈으로 가장 저렴한 숫자를 얼마나 살 수 있는지 구함
remain = M - first_digit[0]
if (remain >= 0):
    last_digit_cnt = remain // data[0][0]
    remain = remain % data[0][0]
else:
    # 0이 아닌 가장 저렴한 숫자를 샀는데 남은돈이 음수라면,
    # 첫자리가 0이고, 더 이상 구매할 수 없음(적어도 하나의 숫자를 살 수 있는 입력만 주어지므로)
    sys.exit(print(0))

# 3. 첫 자리 + 남는 돈 다 털어서 산 가장 저렴한 숫자 concat 하면 자릿수 확정
result = [first_digit[1]] + ([data[0][1]])*last_digit_cnt
# print(f"{result=}")
# print(f"{remain=}")

# 4. 자릿수 확정된 result 리스트를 앞에서 부터 순회하면서 남은 예산 안에서 숫자 교체
for idx, val in enumerate(result):
    budget = remain + P[val]  # 현재 자릿수의 숫자 가격 + 남은 돈이 예산이 됨
    if ((i := bisect_left(data, (budget, 10)))):  # bisect 결과가 0이라면.. 예산이 모자란거
        
        # bisect 한 범위 내에서 살 수 있는 가장 큰 숫자 고름
        tmp = -1
        for j in range(0, i):
            if (data[j][1] > tmp):
                tmp = data[j][1]
                final_idx = j
        
        result[idx] = data[final_idx][1]  # 더 큰 숫자로 교체
        remain = budget - data[final_idx][0]  # 숫자를 구매했으므로 남은 돈 삭감

print(''.join(map(str, result)))

# print(data)