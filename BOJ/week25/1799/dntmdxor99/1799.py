import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def return_idx(i):
    y, x = cand[i][0], cand[i][1]
    idx_right = y + x
    idx_left = n - 1 + y - x

    return idx_right, idx_left      # 좌표를 기준으로 대각선의 인덱스를 반환함


def backtracking(cnt, i):
    if cnt == 0:        # 해당 갯수를 모두 넣을 수 있음
        return True
    
    elif i == l - 1:        # 해당 갯수를 모두 못 넣었는데, 넣을 수 있는 곳이 없음
        return False

    for j in range(i + 1, l):

        idx_right, idx_left = return_idx(j)

        if right[idx_right] and left[idx_left]:     # 대각선 둘 다 확인 결과 넣을 수 있음
            right[idx_right] = False        # 이제 해당 대각선 자리들에는 못 넣음
            left[idx_left] = False

            if backtracking(cnt - 1, j):
                return True
            else:
                right[idx_right] = True
                left[idx_left] = True
    else:
        return False        # 모든 가능성을 살폈는데, 하나도 안 됨


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    cand = list()
    for i in range(n):
        for j in range(n):
            if maps[i][j]:
                cand.append((i, j))
    
    l = len(cand)
    start, end = 1, l
    right, left = [True] * (2 * n - 1), [True] * (2 * n - 1)

    ans = 0
    
    while start < end:
        mid = (start + end) // 2

        for i in range(l):
            idx_right, idx_left = return_idx(i)
            right[idx_right] = False
            left[idx_left] = False

            if backtracking(mid - 1, i):     # 만약 True라면 mid는 가능함, 놓았으므로 mid - 1로 시작함
                ans = mid
                start = mid + 1
                break

            right[idx_right] = True
            left[idx_left] = True

        else:       # 만약 break가 나지 않았다면
            end = mid

    print(ans)