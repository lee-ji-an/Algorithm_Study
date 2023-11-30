def solution(p):
    # '올바른 괄호 문자열'인지 검사하는 함수
    def is_right(p):
        b_cnt = 0
        for i in range(len(p)):
            if p[i] == '(':
                b_cnt += 1
            else:
                b_cnt -= 1

            if b_cnt < 0:
                return False

        return True

    # 전체 문자열을 두 문자열 u, v로 분리하는 함수
    def split_string(p):
        b_cnt = 0
        for i in range(len(p)):
            if p[i] == '(':
                b_cnt += 1
            else:
                b_cnt -= 1

            if b_cnt == 0:
                return p[:i + 1], p[i + 1:]

        return p, ""

    # 전체 문자열의 앞뒤 문자를 제거하고, 괄호 방향을 뒤집는 함수
    def reverse(p):
        r = {"(": ")", ")": "("}
        return ''.join([r[p[i]] for i in range(1, len(p) - 1)])

    def dfs(p):
        if p == "" or is_right(p):
            return p

        # 두 문자열로 쪼개기
        u, v = split_string(p)

        # 재귀를 이용해 "올바른 괄호 문자열"로 변환
        if is_right(u):
            return u + dfs(v)
        else:
            return "(" + dfs(v) + ")" + reverse(u)

    return dfs(p)
