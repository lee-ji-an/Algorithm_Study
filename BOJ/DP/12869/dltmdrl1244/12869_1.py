n = int(input())
scv = list(map(int, input().split()))
while len(scv) != 3:
    scv.append(0)

dp = [[[22] * (61) for _ in range(61)] for _ in range(61)]

ans = 100
def attack(s, cnt):
    global ans
    a, b, c = s
    # 셋 다 죽었으면 ans 갱신
    if a <= 0 and b <= 0 and c <= 0:
        ans = min(ans, cnt)
        return

    # 이미 죽은 scv에 대해 체력이 음수가 되면 dp 배열을 참조하지 못하므로 0으로 처리
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    if c < 0:
        c = 0

    # 이미 더 적은 공격횟수로 해당 상태에 도달할 수 있었다면 더 보지 않는다
    if dp[a][b][c] <= cnt:
        return
    dp[a][b][c] = cnt

    # 죽지 않았으면 때릴 수 있다
    if a != 0:
        attack([a-9, b-3, c-1], cnt + 1)
        attack([a-9, b-1, c-3], cnt + 1)
    if b != 0:
        attack([a-3, b-9, c-1], cnt + 1)
        attack([a-1, b-9, c-3], cnt + 1)
    if c != 0:
        attack([a-3, b-1, c-9], cnt + 1)
        attack([a-1, b-3, c-9], cnt + 1)

attack(scv, 0)
print(ans)