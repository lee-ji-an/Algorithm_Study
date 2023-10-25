def solution(number, K):
    N = len(number)
    number = list(map(int, number))

    stack = []
    popCnt = 0

    for digit in number:
        while (stack and stack[-1] < digit and popCnt < K):
            stack.pop()
            popCnt += 1
        stack.append(digit)

    return ''.join(map(str, stack[:N-K]))
