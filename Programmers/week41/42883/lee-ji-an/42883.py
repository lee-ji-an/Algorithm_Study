def solution(number, k):
    stack = []

    for s in number:
        while k > 0 and stack:
            # stack의 top value 와 현재 탐색 값을 비교
            if stack[-1] >= int(s):
                break
            stack.pop()
            k -= 1
        stack.append(int(s))

    answer = ''.join(map(str, stack[:len(number) - k]))
    return answer
