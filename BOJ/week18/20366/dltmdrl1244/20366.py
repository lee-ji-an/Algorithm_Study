import sys
input = sys.stdin.readline


def logic(elsa, left, right):
    # elsa의 범위 안에서 선택하여 최솟값을 반환함
    val = sys.maxsize

    while left < right:
        anna = maps[left] + maps[right]
        if elsa > anna:     # 엘사가 더 크다면 안나를 키워야 함
            left += 1
        elif elsa < anna:       # 그 반대로
            right -= 1
        else:       # 만약 둘이 같다면 0이 되는 최솟값이 나오는 것이므로 끝냄
            print(0)
            exit(0)

        val = min(val, abs(elsa - anna))        # 최솟값을 반환해야 함

    return val


if __name__ == "__main__":
    n = int(input())
    maps = list(map(int, input().split()))
    maps.sort()

    ans = sys.maxsize
    for i in range(n):
        for j in range(n - 1, max(i + 2, 0), -1):
            # elsa의 범위를 줄임. 이때 안에 최소 2개의 원소는 들어갈 수 있도록 만들어야 함
            ans = min(ans, logic(maps[i] + maps[j], i + 1, j - 1))

    print(ans)