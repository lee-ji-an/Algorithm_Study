import sys
from collections import defaultdict
input = sys.stdin.readline


def isPalin(string):
    return string == string[::-1]

arr = input().rstrip()
n = len(arr)
dp = [0] + [i+1 for i in range(n)]
alphabet = defaultdict(list)

# 각 알파벳이 등장하는 위치를 인덱스로 기록해 놓는다
for idx, letter in enumerate(arr):
    alphabet[letter].append(idx)

for i in range(n+1):
    # 이전에 이 알파벳이 등장했던 곳을 찾는다
    for prev in alphabet[arr[i-1]]:
        if prev > i:
            break
        
        # 그 곳부터 i번째까지 하나의 팰린드롬으로 묶을 수 있다면 dp[그 이전] + 1로 줄일 수 있다
        if isPalin(arr[prev:i]):
            dp[i] = min(dp[i], dp[prev] + 1)
    
    # 만약 팰린드롬이 없다면 이전 dp값에서 새 글자 하나짜리 팰린드롬을 더한 +1
    dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[-1])