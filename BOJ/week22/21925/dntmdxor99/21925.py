import sys
input = sys.stdin.readline


def check(cur):
    l = len(stack)
    for i in range(l):

        if cur + i >= n:
            print(-1)
            exit(0)

        if stack[-i - 1] != maps[cur + i]:
            return False, 0

    stack.clear()
    return True, cur + l


if __name__ == "__main__":
    n = int(input())
    maps = list(map(int, input().split()))

    stack = []
    ans = 0
    i = 0

    while i < n:
        if len(stack) == 0:
            stack.append(maps[i])
            i += 1
        else:
            flag, next = check(i)
            if flag:
                ans += 1
                i = next
            else:
                stack.append(maps[i])
                i += 1

    if len(stack) > 0:
        print(-1)
    else:
        print(ans)
