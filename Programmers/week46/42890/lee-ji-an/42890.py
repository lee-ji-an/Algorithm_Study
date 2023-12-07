def solution(relation):
    from itertools import combinations
    answer_set = set()

    for i in range(1, len(relation[0])):
        for combi in combinations(range(len(relation[0])), i):
            # 유일성 검사 : 현재 확인하고 있는 칼럼에 따라 아레와 같이 스트링을 만들어서 같은 row가 있는지 비교
            # attr1+attr2+...
            flag = True
            attr_set = set()
            for rel in relation:
                attr = ""
                for c in combi:
                    attr += rel[c]
                    attr += '+'

                if attr in attr_set:
                    flag = False
                    break

                attr_set.add(attr)

            # 최소성 검사
            if flag:
                for ans in answer_set:
                    if set(ans).issubset(combi):
                        break
                else:
                    answer_set.add(combi)

    if answer_set:
        return len(answer_set)
    else:
        return 1
