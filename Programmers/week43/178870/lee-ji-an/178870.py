def solution(sequence, k):
    answer = [0, float('inf')]
    start_ptr, end_ptr = 0, 0
    total = sequence[0]

    while True:
        # 시작 포인터 오른쪽으로 한 칸 이동
        if total >= k:
            # 합이 k이면서 수열의 길이가 더 짧다면 정답 배열을 갱신
            if total == k and end_ptr - start_ptr < answer[1] - answer[0]:
                answer[0] = start_ptr
                answer[1] = end_ptr
            total -= sequence[start_ptr]
            start_ptr += 1
        # 끝 포인터 오른쪽으로 한 칸 이동
        else:
            end_ptr += 1
            if end_ptr >= len(sequence):
                break
            total += sequence[end_ptr]

    return answer
