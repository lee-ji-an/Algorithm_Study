def solution(s):
    N = len(s)
    answer = float('inf')
    for l in range(1, N + 1):
        total_len = 0
        prev_spell = ""
        same_cnt = 0

        for i in range(0, N, l):
            spell = s[i: i + l]
            # 이전 문자열과 현재 문자열이 일치할 때
            if spell == prev_spell:
                same_cnt += 1
                # 중복된 횟수의 자릿수가 증가할 때 전체 길이를 1씩 증가시킴
                if same_cnt == 1 or same_cnt == 9 or same_cnt == 99 or same_cnt == 999:
                    total_len += 1
            # 이전 문자열과 현재 문자열이 일치하지 않을 때
            else:
                total_len += min(l, N - i)
                same_cnt = 0
            prev_spell = spell

        answer = min(answer, total_len)

    return answer
