def solution(arr):
    N = len(arr)
    from collections import Counter
    cnt = [0, 0]
    for a in arr:
        count = Counter(a)
        cnt[0] += count[0]
        cnt[1] += count[1]

    # N * N -> 2 * 2 순서로 압축 가능한 경우를 탐색
    length = N
    while length > 1:
        for i in range(N // length):
            for j in range(N // length):
                value = arr[i * length][j * length]
                if value == -1:
                    continue

                flag = True
                for r in range(length):
                    for c in range(length):
                        row, col = i * length + r, j * length + c
                        # 압축할 수 없는 경우
                        if arr[row][col] != value:
                            flag = False
                            break
                    if not flag: break

                # 압축 가능한 경우를 찾았을 때
                # arr을 -1로 표시 / 0 or 1 개수 줄이기
                if flag:
                    for r in range(length):
                        for c in range(length):
                            row, col = i * length + r, j * length + c
                            arr[row][col] = -1
                    cnt[value] -= length * length - 1
        length //= 2

    return cnt
