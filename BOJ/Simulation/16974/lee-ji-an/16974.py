import sys
input = sys.stdin.readline

N, X = map(int, input().split())


def recursion(lv, x):
    if x == 0:
        return 0
    if x == total[lv]:
        return patty[lv]

    if x <= total[lv - 1] + 2:  # x 가 중간에 패티가 들어가는 지점보다 같거나 왼쪽일 때
        if x == total[lv - 1] + 2:
            return patty[lv - 1] + 1  # x 가 중간에 패티가 들어가는 지점까지일 때
        else:
            return recursion(lv - 1, x - 1)  # # x 가 중간에 패티가 들어가는 지점보다 왼쪽일 때
    else:
        return patty[lv - 1] + 1 + recursion(lv - 1, x - total[lv - 1] - 2)  # # x 가 중간에 패티가 들어가는 지점보다 오른쪽일 때


total = [1] * (N + 1)
patty = [1] * (N + 1)
for i in range(1, N + 1):
    total[i] = total[i - 1] * 2 + 3  # level i 의 전체 햄버거 장 수 (패티 + 번)
for i in range(1, N + 1):
    patty[i] = patty[i - 1] * 2 + 1  # level i 의 전체 패티 장 수
print(recursion(N, X))
