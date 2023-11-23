def solution(info, query):
    import bisect
    answer = []
    info_dict = {'python': set(), 'java': set(), 'cpp': set(), 'backend': set(), 'frontend': set(), 'junior': set(),
                 'senior': set(), 'chicken': set(), 'pizza': set()}
    # info_dict에 분류하기
    score_person = []
    real_score = []
    score = []
    for i in range(len(info)):
        person_info = tuple(info[i].split())
        for j in range(4):
            info_dict[person_info[j]].add(i)
        # score에 (score, student) 형태로 저장
        score.append((int(person_info[4]), i))
    score.sort()

    # score, 사람을 따로 저장
    for s in score:
        score_person.append(s[1])
        real_score.append(s[0])

    # 쿼리에 해당하는 사람 정보 찾기
    for q in query:
        res_person = set(i for i in range(len(info)))
        keywords = q.split()
        for i in range(0, 7, 2):
            if keywords[i] == '-':
                continue
            res_person = res_person.intersection(info_dict[keywords[i]])

        # 이분 탐색으로 찾고자 하는 점수보다 높은 사람 구하기
        idx = bisect.bisect_left(real_score, int(keywords[7]))
        res_person = res_person.intersection(set(score_person[idx:]))
        answer.append(len(res_person))

    return answer
