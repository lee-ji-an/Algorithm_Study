import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(T):
    function = input().rstrip()
    length = int(input())

    # 괄호 제거해서 저장
    array = deque(list(input()[1: -2].split(',')))
    ptr = True  # 방향을 결정
    for f in function:
        if f == 'R':
            ptr = not ptr
        else:
            if length == 0:  # 'error' 인 경우
                print("error")
                break
            if ptr:
                array.popleft()
            else:
                array.pop()
            length -= 1
    else:
        if not ptr:
            array.reverse()

        # 결과 출력
        print('[', end="")
        if array:
            print(array[0], end="")
            for i in range(1, len(array)):
                print(',', end="")
                print(array[i], end="")
        print(']')
