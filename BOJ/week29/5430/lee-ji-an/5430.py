import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(T):
    function = input().rstrip()
    length = int(input())

    if length == 0:  # 리스트 길이가 0일 때 처리
        input()
        if 'D' in function:
            print("error")
        else:
            print([])
        continue

    # 괄호 제거해서 저장
    array = deque(list(map(int, input()[1: -2].split(','))))

    ptr = True  # 방향을 결정
    for f in function:
        if f == 'R':
            ptr = not ptr
        else:
            if not array:  # 'error' 인 경우
                break
            if ptr:
                array.popleft()
            else:
                array.pop()
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
        continue

    # error 출력
    print("error")
