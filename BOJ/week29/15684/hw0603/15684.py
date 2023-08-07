import sys

N, M, H = map(int, sys.stdin.readline().strip().split())
ladder = [[None]*(N+1) for _ in range(H+1)]


for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    ladder[a][b] = (a, b+1)
    ladder[a][b+1] = (a, b)


def isValidate(ladder):
    for playerIdx in range(1, N+1):
        currentPos = playerIdx

        for depth in range(1, H+1):
            if (val := ladder[depth][currentPos]):
                a, b = val
                currentPos = b

        if (playerIdx != currentPos):
            return False

    return True


def dfs(ladder, cnt, d, p):
    global ans
    if (ans <= cnt):  # 가로선을 정답보다 많이 만든 경우 더 이상 확인 필요 X
        return
    if (isValidate(ladder)):  # 현재 사다리판의 상태가 종료조건인지 검사
        ans = min(ans, cnt)
        return
    if (cnt == 3):
        return
    for depth in range(d, H+1):
        # k = p if depth == d else 0  # 같은 세로줄(p)을 확인하는 경우 p부터 확인. 다르다면 0부터
        k = 0
        for pos in range(k, N):
            if (ladder[depth][pos] is None and ladder[depth][pos+1] is None):  # 가로선 놓을 수 있는 경우 가로선 놓아 봄
                ladder[depth][pos] = (depth, pos+1)
                ladder[depth][pos+1] = (depth, pos)
                dfs(ladder, cnt + 1, depth, pos + 2)  # 연속된 가로선을 만들지 않기 위해 pos+2로 호출
                ladder[depth][pos] = None
                ladder[depth][pos+1] = None


ans = 4
dfs(ladder, 0, 1, 1)
print(ans if ans <= 3 else -1)
