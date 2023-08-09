import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        p = list(input().strip())
        n = int(input())
        maps = deque(input()[1:-2].split(','))

        sequence = True     # 순방향
        for inst in p:
            match inst:
                case 'R': sequence = not sequence
                case 'D':
                    if n > 0:
                        maps.popleft() if sequence else maps.pop()
                        n -= 1
                    else:
                        print('error')
                        break

        else:
            print('[', end='')
            print(','.join(maps), end='') if sequence else print(','.join(reversed(maps)), end='')
            print(']')