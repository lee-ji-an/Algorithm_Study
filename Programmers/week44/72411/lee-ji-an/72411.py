def solution(orders, course):
    from itertools import combinations
    answer = []

    for cnt in course:
        max_cnt = 0
        menu_dict = dict()
        for order in orders:
            # 손님이 주문한 메뉴에서 가능한 조합을 모두 탐색
            for i in combinations(order, cnt):
                # 단품메뉴 조합을 정렬한 뒤 다시 조합
                menu = ''.join(sorted(list(i)))

                if menu in menu_dict:
                    menu_dict[menu] += 1
                else:
                    menu_dict[menu] = 1

                max_cnt = max(max_cnt, menu_dict[menu])

        # 최대 주문 횟수와 일치하는 메뉴를 탐색하여 저장
        if max_cnt >= 2:
            for key in menu_dict:
                if menu_dict[key] == max_cnt:
                    answer.append(key)

    return sorted(answer)
