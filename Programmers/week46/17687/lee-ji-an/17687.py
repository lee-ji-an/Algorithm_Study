def solution(n, t, m, p):
    answer = ''
    num_value = 0
    num_to_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    # 숫자를 n진수 스트링으로 변환시키는 함수
    def to_str(number):
        if number == 0:
            return '0'

        string = ''
        temp = number
        while temp > 0:
            string = num_to_str[temp % n] + string
            temp = temp // n

        return string

    # 정답을 도출할 수 있는 길이를 충족했는지 확인
    min_length = m * (t - 1) + p
    while min_length > len(answer):
        answer += to_str(num_value)
        num_value += 1

    return answer[p - 1::m][: t]
