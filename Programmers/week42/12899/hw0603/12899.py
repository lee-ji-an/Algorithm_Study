def solution(n):
    data = []
    while (n):
        remainder = n % 3
        if (remainder == 0):
            # 3으로 나눠 떨어지는 숫자는 몫을 -1 해서 다시 나눔
            data.append('4')  # '3'을 넣어야 하지만, 3대신 4를 사용하므로 '4'를 삽입
            n = (n // 3) - 1
        else:
            data.append(str(remainder))
            n //= 3

    return ''.join(reversed(data))
