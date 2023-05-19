if __name__ == "__main__":
    n = int(input())

    maps = [i**2 for i in range(1, n)]      # (n-1)^2 - (n-2)^2 > n if n > 2, 따라서 n - 1까지 제곱수를 구해도 상관 없음
    # 1, 2는 아래의 while 문의 n - 1에서 처리됨

    left = 0
    right = 1
    ans = []

    while left < right < n - 1:     # right가 left보다 항상 크도록
        val = maps[right] - maps[left]
        if val > n:     # val이 더 크다면 왼쪽 포인터를 옮겨야 함
            left = min(left, n - 2) + 1
        elif val < n:       # val이 더 작다면 오른쪽 포인터를 옮겨야 함
            right = min(right, n - 2) + 1
        else:       # 같다면 후보지에 추가, 양쪽 다 옮겨도 상관 없음
            ans.append(right + 1)
            left += 1
            right += 1

    if ans:
        print(*ans, sep='\n')
    else:
        print(-1)

