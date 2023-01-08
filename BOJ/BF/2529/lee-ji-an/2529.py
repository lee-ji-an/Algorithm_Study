import sys


def dfs2(depth):
    global flag
    if depth == n+1:
        if inequality(combi):
            flag = False
            return
    for idx in range(0, n+1):
        if flag:
            if visited[idx] == 0:
                combi[depth] = number[idx]
                visited[idx] = 1
                dfs2(depth + 1)
                visited[idx] = 0
        else:
            break

def inequality(data):
    for i in range(0, n):
        if s[i] == '>' and data[i] < data[i+1]:
            return False
        elif s[i] == '<' and data[i] > data[i+1]:
            return False
        else:
            continue
    return True

inputs = sys.stdin.readline
n = int(inputs())
s = input().split()

# 최댓값 구하기
flag = True
visited = [0] * 10
number = [i for i in range(9, 8-n, -1)]
combi = [0] * (n+1)
dfs2(0)
print(''.join(list(map(str, combi))))

# 최솟값 구하기
flag = True
visited = [0] * (n+1)
number = [i for i in range(0, n+1)]
dfs2(0)
print(''.join(list(map(str, combi))))