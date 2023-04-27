import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().split())
    maps = list(map(int, input().split()))
    left = 0
    right = 0
    val = list()

    tmp = 0

    while True:
        if tmp >= k:
            val.append([tmp - k, left, right - 1])
            tmp -= maps[left]
            left += 1
        else:
            tmp += maps[right]
            right = min(right, n - 2) + 1

        if left >= n - 1:
            break

    val.sort(reverse = True)

    maps = [True] * n
    ans = 0

    for rem, left, right in val:
        if maps[left] and maps[right]:
            maps[left: right + 1] = [False] * (right + 1 - left)
            ans += rem

    print(ans)

