def solution(queue1, queue2):
    queue = queue1 + queue2
    middle = (sum(queue1) + sum(queue2)) // 2

    # queue1을 기준으로 큐 안에 있는 수의 합이 middle 이 될 때까지 탐색
    start_ptr = 0
    end_ptr = len(queue1) - 1
    prefix_sum = sum(queue1)

    answer = 0
    while True:
        # queue1에 포함된 수의 합이 middle에 도달하면 정답
        if middle == prefix_sum:
            break

        # start_ptr (왼쪽 포인터)를 옮김
        if prefix_sum > middle:
            if start_ptr >= len(queue1) + len(queue2) - 1:
                break
            prefix_sum -= queue[start_ptr]
            start_ptr += 1
        # end_ptr (오른쪽 포인터)를 옮김
        else:
            if end_ptr >= len(queue1) + len(queue2) - 1:
                break
            end_ptr += 1
            prefix_sum += queue[end_ptr]

        answer += 1

    if middle == prefix_sum:
        return answer
    else:
        return -1
