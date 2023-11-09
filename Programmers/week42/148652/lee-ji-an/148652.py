def solution(n, l, r):
    one_prefix_sum = [0, 1, 2, 2, 3, 4]

    def dfs(n_level, pos):
        # '11011'에서의 1의 갯수를 반환
        if n_level == 1:
            return one_prefix_sum[pos]

        # a 번째 수까지는 1을 모두 카운트 하면 됨, b는 남은 숫자 갯수
        a, b = divmod(pos, 5 ** (n_level - 1))

        if a <= 1:
            return 4 ** (n_level - 1) * a + dfs(n_level - 1, b)
        # a == 2 일 때 는 b를 무시해도 됨 -> 어차피 남은 b의 갯수는 모두 0이기 때문
        elif a == 2:
            return 4 ** (n_level - 1) * a
        else:
            return 4 ** (n_level - 1) * (a - 1) + dfs(n_level - 1, b)

    ans = dfs(n, r) - dfs(n, l - 1)

    return ans
