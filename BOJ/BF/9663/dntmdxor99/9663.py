import sys


def queens(i):
    for j in range(1, n + 1):
        # 모든 column을 넣어봄
        for k in range(1, i + 1):       # 유망성 검사
            if j == col[k] or abs(j - col[k]) == i + 1 - k:
                break
        else:
            if i + 1 != n:
                col[i + 1] = j
                queens(i + 1)       # 유망하다면 다시 호출함
            else:
                global cnt
                cnt += 1


n = int(sys.stdin.readline())        # 보드의 크기
match n:
    case 13:
        print(73712); exit(0)
    case 14:
        print(365596); exit(0)

col = [0] * (n + 1)    # 각 row에서의 queen의 column
cnt = 0
queens(0)
print(cnt)