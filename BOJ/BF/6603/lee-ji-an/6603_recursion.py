import sys

input = sys.stdin.readline

combi = [0] * 6


def dfs(start, depth):
    if depth == 6:
        for j in range(6):
            print(combi[j], end=" ")
        print()
        return
    for i in range(start, k):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)


input_list = list(map(int, input().split()))
while input_list[0] != 0:
    k = input_list[0]
    s = input_list[1:]
    dfs(0, 0)
    print()
    input_list = list(map(int, input().split()))
