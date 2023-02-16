import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))


def dp(num_list):
    dp_case = [{} for _ in range(N)]
    dp_case[0][num_list[0]] = 1
    for i in range(1, N - 1):
        num = num_list[i]
        for key, value in dp_case[i - 1].items():
            if key + num <= 20:
                if key + num in dp_case[i]:
                    dp_case[i][key + num] += dp_case[i - 1][key]
                else:
                    dp_case[i][key + num] = dp_case[i - 1][key]

            if key - num >= 0:
                if key - num in dp_case[i]:
                    dp_case[i][key - num] += dp_case[i - 1][key]
                else:
                    dp_case[i][key - num] = dp_case[i - 1][key]

    if num_list[N - 1] in dp_case[N - 2]:
        return dp_case[N - 2][num_list[N - 1]]
    else:
        return 0


print(dp(num_list))
