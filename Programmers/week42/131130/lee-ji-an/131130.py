def solution(cards):
    visited = [False] * len(cards)
    group_cnt = []
    for i in range(len(cards)):
        # 아직 방문 안 한 상자를 발견하면 탐색 시
        if not visited[i]:
            res = i
            cnt = 0
            # 그룹에 속한 상자의 수 구하기
            while not visited[res]:
                visited[res] = True
                cnt += 1
                res = cards[res] - 1
            group_cnt.append(cnt)

    # 최대 점수 구하기
    if len(group_cnt) <= 1:
        return 0
    else:
        group_cnt.sort(reverse=True)
        return group_cnt[0] * group_cnt[1]
