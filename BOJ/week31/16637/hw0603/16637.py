import sys

N = int(sys.stdin.readline())
exp = list(sys.stdin.readline().strip())
ans = -sys.maxsize


def calc(*args):
    return str(eval(''.join(args)))


def dfs(pos, val):
    global ans
    
    # 종료조건: 현재 위치가 끝에 도달하면
    if (pos == N):
        ans = max(ans, int(val))  # 최댓값 갱신하고 해당 가지 종료
        return
    
    # 현재 위치에 괄호 추가 -> pos+2 위치의 연산자를 먼저 연산 하고 pos+4로 이동
    if (pos+4 <= N):
        dfs(
            pos+4,
            calc(
                val,  # 3
                exp[pos],  # +
                calc(exp[pos+1], exp[pos+2], exp[pos+3])  # (8*7)
            )
        )
    # 현재 위치에 괄호 없음 -> 바로 뒤의 숫자와 연산 하고 pos+2로 이동
    if (pos+2 <= N):
        dfs(
            pos+2,
            calc(
                val,  # 3
                exp[pos],  # +
                exp[pos+1]  # 8
            )
        )


dfs(1, exp[0])  # Expression의 첫 숫자와, exp[1](=첫 연산자)를 가지고 재귀호출 시작
print(ans)
