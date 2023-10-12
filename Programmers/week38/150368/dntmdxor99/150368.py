# 할인율이 증가 -> 구매 인원 증가 -> 구매 비용 증가 -> 서비스 가입 증가
# 할인율이 더 증가 -> 구매 인원 증가 -> 하지만 구매 비용 감소 -> 서비스 가입 감소
# BF일 때 -> 4^7 * 100 = 160만

from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    l_em = len(emoticons)
    l_user = len(users)
    
    max_subscriber = 0
    max_profit = 0
    
    em_discount = [[i * j // 10 for i in range(9, 5, -1)] for j in emoticons]
    
    for discounts in product([40, 30, 20, 10], repeat = l_em):
        subscriber = 0
        profit = 0
        
        for user in users:
            user_profit = 0
            
            for i in range(l_em):
                if discounts[i] >= user[0]:     # 할인율이 유저의 구매 허용 비율보다 높다면
                    user_profit += em_discount[i][discounts[i] // 10 - 1]     # 할인된 금액을 넣음
                    
            if user_profit >= user[1]:
                subscriber += 1
            else:
                profit += user_profit
        
        answer = max(answer, [subscriber, profit])
    
    return answer