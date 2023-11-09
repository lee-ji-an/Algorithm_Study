def solution(n):
    num_dict = {1: '1', 2: '2', 3: '4'}
    answer = ''

    while n > 0:
        # d 는 1, 2, 3 중 하나 -> 맨 끝자리부터 차례대로 d 에 저장됨
        d = n % 3 if n % 3 != 0 else 3

        # 정답 문자열에 추가
        answer = num_dict[d] + answer

        # 수의 자리 수를 한 칸 오른쪽으로 옮기는 작업
        n = (n - d) // 3

    return answer
