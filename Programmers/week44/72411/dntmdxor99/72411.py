from itertools import combinations

def solution(orders, course):
    answer = []
    maps = {}
    orders = [''.join(sorted(list(order))) for order in orders]     # 미리 문자 순서대로 정렬해놓음
    
    for cnt in course:      # 조합에 들어가는 음식 개수
        maps.clear()        # 다음 시행을 위해 딕셔너리 초기화   
        for order in orders:        # 단품메뉴 조합
            for i in combinations(order, cnt):      # 조합을 찾음
                mix = ''.join(i)
                maps[mix] = maps.get(mix, 0) + 1        # 모두 딕셔너리에 입력한다.
                
        lsts = sorted(maps.items(), key = lambda x : x[1], reverse = True)      # items()를 모두 반환한 후, 리스트로 만들어서 가장 많은 개수를 찾음
        cnt = 2
        for lst in lsts:
            if lst[1] >= cnt:
                answer.append(lst[0])
                cnt = lst[1]
            else:
                break
    
    answer.sort()
    return answer