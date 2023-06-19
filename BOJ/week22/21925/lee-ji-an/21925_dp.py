import sys
input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
palindrome = [[False] * (N//2) for _ in range(N//2)]

# i ~ j 가 팰린드롬인지 판단해 2차원 리스트( palindrome[i][j] )에 저장
for i in range(N//2):  # 길이가 2인 팰린드롬 판단
    if sequence[i * 2] == sequence[i * 2 + 1]:
        palindrome[i][i] = True

for i in range(1, N//2):
    for j in range(0, N//2 - i):
        # j ~ j + i
        if j + 1 > j + i - 1 or palindrome[j + 1][j + i - 1]:
            # 바깥쪽끼리 비교, 안쪽끼리 비교
            if sequence[j * 2] == sequence[(j + i) * 2 + 1] and sequence[j * 2 + 1] == sequence[(j + i) * 2]:
                palindrome[j][j + i] = True


dp = [0] * (N//2)
dp[0] = 1 if palindrome[0][0] else 0

for i in range(1, N//2):  # i 를 끝으로 하는 짝수 팰린드롬의 최대 갯수
    max_value = 1 if palindrome[0][i] else 0

    for j in range(i, -1, -1):
        if palindrome[j][i] and dp[j - 1] > 0:
            max_value = max(max_value, dp[j - 1] + 1)
            break

    dp[i] = max_value

print(dp[-1] if dp[-1] > 0 else -1)
