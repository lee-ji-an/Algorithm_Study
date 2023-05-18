import sys
input = sys.stdin.readline


if __name__ == "__main__":
    maps = list(input().strip())

    left = 0
    right = 0
    total = 0
    ans = 0

    for i in maps:
        if i == '(':
            left += 1
            total += 1
        else:
            right += 1
            total -= 1

        if total == 1:
            # 1이라면 여는 괄호가 더 많음.
            # 따라서 앞으로 닫는 괄호가 더 적다면, 지금부터 나오는 여는 괄호가 모두 후보자임
            left = 0

        if total == -1:
            # 만약 -1이라면 닫힌 괄호가 더 많은 상태임
            # 따라서 지금까지 나온 닫힌 괄호가 모두 후보자임
            ans = right
            break

    if total == 2:
        # 여는 괄호가 더 많은 상태이므로, 아까 초기화 한 이후부터 나온 모든 여는 괄호의 개수가 정답임
        ans = left

    print(ans)
