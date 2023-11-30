def solution(places):
    from itertools import combinations
    answer = []

    # 사람이 존재하는 위치를 저장
    for place in places:
        person_pos = []
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    person_pos.append((r, c))

        # 사람이 존재하는 위치 중 2개를 골라 거리두기를 위반하는지 확인
        res = 1
        for combi in combinations(person_pos, 2):
            x_dist, y_dist = combi[0][0] - combi[1][0], combi[0][1] - combi[1][1]
            # 맨해튼 거리가 1인 모든 경우는 거리두기 위반
            if abs(x_dist) + abs(y_dist) == 1:
                res = 0
                break
            # 맨해튼 거리가 2인 경우
            elif abs(x_dist) + abs(y_dist) == 2:
                # o -
                # - o
                if abs(x_dist) == 1 and abs(y_dist) == 1:
                    if not (place[combi[0][0]][combi[1][1]] == 'X' and place[combi[1][0]][combi[0][1]] == 'X'):
                        res = 0
                        break
                else:
                    # o - o
                    if combi[0][0] == combi[1][0]:
                        if place[combi[0][0]][(combi[0][1] + combi[1][1]) // 2] != 'X':
                            res = 0
                            break
                    # o
                    # -
                    # o
                    else:
                        if place[(combi[0][0] + combi[1][0]) // 2][combi[0][1]] != 'X':
                            res = 0
                            break
        answer.append(res)

    return answer
