import sys
input = sys.stdin.readline

if __name__ == "__main__":
    maps = list(input().strip())

    left_cnt, right_cnt = [], []

    # K의 개수를 세서 각 R의 자리에 넣어줌
    cnt = 0
    for i in maps:
        if i == 'K':
            cnt += 1
        else:
            left_cnt.append(cnt)

    cnt = 0
    for i in maps[::-1]:
        if i == 'K':
            cnt += 1
        else:
            right_cnt.append(cnt)
    right_cnt.reverse()

    left = 0
    right = len(right_cnt) - 1
    ans = 0

    while left <= right:
        ans = max(ans, right - left + 1 + min(left_cnt[left], right_cnt[right]) * 2)
        # 구간에서 R의 개수는 right - left + 1이고, 바깥의 K의 개수는 위의 min(~~) * 2개임
        if left_cnt[left] < right_cnt[right]:
            left += 1
        elif left_cnt[left] > right_cnt[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    print(ans)
