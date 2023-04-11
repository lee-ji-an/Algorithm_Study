import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(flag):
    stack = [(100001, 0)]       # 언더플로우 방지
    if flag:
        lst.reverse()       # 오른쪽에서 왼쪽으로 보기 위해, 이렇게 된다면 내 오른쪽만 바라봄
    for i in lst:
        while maps[i] >= stack[-1][0]:      # 나보다 작은 애들은 일단 팝함
            stack.pop()
        else:
            count[i] += len(stack) - 1      # 길이 -1을 넣어야 함

            match flag:
                case True:
                    what_right = stack[-1][1]       # 내 오른쪽에 나보다 큰 애의 인덱스
                    if count[i]:
                        if what[i] and what_right:
                            left = abs(i + 1 - what[i])     # 왼쪽까지 거리
                            right = abs(what_right - i - 1)     # 오른쪽까지 거리
                            if left > right:        # 왼쪽과 거리가 더 크다면, 오른쪽을 넣는게 맞음
                                what[i] = what_right
                        elif what_right:        # 왼쪽에서 나보다 큰 애의 인덱스가 0이라면, 오른쪽을 넣는게 맞음
                            what[i] = what_right
                case False:
                    what[i] = stack[-1][1]      # 내 왼쪽에 나보다 큰 애의 인덱스
            stack.append((maps[i], i + 1))      # 그리고 스택에 넣음


if __name__ == "__main__":
    n = int(input())
    maps = list(map(int, input().split()))
    lst = [*range(n)]

    count = [0] * n
    what = [0] * n

    sol(False)
    sol(True)

    for i in range(n):
        print("%d " % count[i])
        if count[i]:
            print("%d" % what[i])
        print("\n")
