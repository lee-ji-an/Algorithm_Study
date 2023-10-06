def solution(k, tangerine):
    # 귤의 크기를 key, 귤의 갯수를 value 로 하는 딕셔너리 생성
    tan_dict = {}
    for t in tangerine:
        if t not in tan_dict:
            tan_dict[t] = 1
        else:
            tan_dict[t] += 1

    # 귤의 갯수를 역순으로 정렬
    tan_list = list(tan_dict.values())
    tan_list.sort(reverse=True)

    # 귤의 갯수를 큰 것부터 탐색 -> 탐색한 귤의 총 갯수가 k 개를 넘어가면 반복문을 중지
    answer = 0
    cnt = k
    for i in tan_list:
        cnt -= i
        answer += 1
        if cnt <= 0:
            break

    return answer
