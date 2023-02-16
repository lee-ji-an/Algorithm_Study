import sys

input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()


def dp(str1, str2):
    dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    prev = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    len1, len2 = len(str1), len(str2)
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                prev[i][j] = (i - 1, j - 1)
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    prev[i][j] = (i - 1, j)
                else:
                    dp[i][j] = dp[i][j - 1]
                    prev[i][j] = (i, j - 1)
    row, col = len1, len2
    ans = []
    cur_lcs = dp[row][col]
    while True:
        if dp[row][col] == 0:
            break
        if cur_lcs > dp[prev[row][col][0]][prev[row][col][1]]:
            ans.append(string1[row - 1])
        row, col = prev[row][col][0], prev[row][col][1]
        cur_lcs = dp[row][col]

    return ans, dp[len1][len2]


lcs_string, max_length = dp(string1, string2)
print(max_length)
for i in range(len(lcs_string) - 1, -1, -1):
    print(lcs_string[i], end="")
print()
