import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    maps = list(map(int, input().split()))

    left = 0
    right = n - 1
    val = 0

    while left < right:
        # min 값을 넣으므로, 작은 애의 포인터를 옮기면 된다. 그래야 min 값이 개선될 여지가 보이기 때문
        inner = right - left - 1
        if maps[left] < maps[right]:
            val = max(val, inner * maps[left])
            left += 1
        elif maps[left] > maps[right]:
            val = max(val, inner * maps[right])
            right -= 1
        else:
            val = max(val, inner * maps[left])
            left += 1
            right -= 1
            """
            left += 1을 하고, right -= 1을 해도 괜찮은 이유
            포인터는 현재 양 끝의 3과 3을 가리키고 있는 상태

            1. 3 7 ... 9 3 혹은 3 9 ... 7 3
                한 쪽만 옮겨봤자 어차피 3이 min 값임 -> 안의 개발자 개수가 줄기 때문에 손해임 -> 둘 다 옮겨도 상관 없음
            2. 3 2 ... 2 3
                한 쪽만 옮겨봤자 어차피 2가 min 값임 -> 위와 동일
            3. 3 2 ... 9 3
                min 값이 2가 되거나, 3이 됨 -> 기존의 값의 이하가 되기 때문에 손해임 -> 둘 다 옮겨도 상관 없음
            """

    print(val)
