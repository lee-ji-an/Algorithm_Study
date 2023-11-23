def solution(name):
    from collections import deque
    answer = 0
    end_pos = 0
    name_list = deque(list(name))
    move = float('inf')

    for j in range(len(name_list)):
        # A가 아닌 수가 등장하는 가장 마지막 인덱스를 구함
        for i in range(len(name_list) - 1, -1, -1):
            if name_list[i] == 'A':
                continue
            end_pos = i
            break
        # j : 문자열을 회전시킨 횟수 (왼쪽으로 갔다가 오른쪽으로 가는 경우)
        # end_pos - j : (오른쪽으로 갔다가 왼쪽으로 가는 경우)
        move = min(move, min(j, abs(end_pos - j)) + end_pos)

        # 문자열을 회전시킴
        name_list.appendleft(name_list.pop())
    answer += move

    # 알파벳을 변경하기 위해서 조이스틱을 조작하는 경우 구하기
    for i in range(len(name)):
        if name[i] == 'A':
            continue
        answer += min(ord(name[i]) - ord('A'), 26 - (ord(name[i]) - ord('A')))

    return answer
