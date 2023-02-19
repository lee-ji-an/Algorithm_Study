import sys

input = sys.stdin.readline

N, S = map(int, input().split())
set_list = list(map(int, input().split()))
cnt = 0


def dfs(depth, value):
    global cnt
    if depth == N:
        return

    dfs(depth + 1, value + set_list[depth])    # 입력 리스트 중에서 depth 번째 수를 포함하는 경우
    if value + set_list[depth] == S:           # 새로운 수를 포함하는 경우에 함수가 끝나고 나서 cnt 를 올려야 함
        cnt += 1
    dfs(depth + 1, value)                      # 입력 리스트 중에서 depth 번째 수를 포함하지 않는 경우


dfs(0, 0)
print(cnt)
