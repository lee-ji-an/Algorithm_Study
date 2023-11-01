def solution(expression):
    from itertools import permutations
    from collections import deque
    n = ""
    op = deque()
    numbers = deque()
    cnt = 0
    answer = 0

    # 숫자를 연산하는 함수
    def calcul(operator, num1, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        else:
            return num1 * num2

    # numbers, operator 파싱해서 리스트에 저장
    for s in expression:
        if 0 <= (ord(s) - ord('0')) <= 9:
            n = n + s
        else:
            numbers.append(int(n))
            n = ""
            op.append(s)
            cnt += 1
    numbers.append(int(n))

    # 순열로 연산자 우선순위의 모든 경우의 수를 탐색
    for perm in permutations(['*', '+', '-'], 3):
        temp_op = deque([_ for _ in op])
        temp_numbers = deque([_ for _ in numbers])

        # 우선순위가 가장 높은 연산자 -> 낮은 연산자 순서대로 먼저 계산
        for p in perm:
            for i in range(len(temp_op)):
                # 현재 탐색하고 있는 연산자라면 계산
                if temp_op[0] == p:
                    num1 = temp_numbers.popleft()
                    num2 = temp_numbers.popleft()
                    cur_op = temp_op.popleft()

                    temp_numbers.appendleft(calcul(cur_op, num1, num2))
                # 현재 탐색하고 있는 연산자가 아니면 계산 안 하고 그대로 큐 맨 뒤에 넣음
                else:
                    temp_numbers.append(temp_numbers.popleft())
                    temp_op.append(temp_op.popleft())

            # 마지막 남은 수는 한 번 더 큐의 뒤로 넣어줘야 함
            temp_numbers.append(temp_numbers.popleft())
        answer = max(answer, abs(temp_numbers[0]))

    return answer
