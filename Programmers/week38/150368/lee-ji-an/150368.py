def solution(users, emoticons):
    discount = [10, 20, 30, 40]

    # 이모티콘 할인 비율 조합을 만드는 함수
    def dfs(order):
        if order == len(emoticons):
            # 이모티콘 구입 결과를 계산하는 함수 호출
            plus_users, total_purchase = calcul(emo_rate)
            if plus_users > result[0]:
                result[0] = plus_users
                result[1] = total_purchase
            elif plus_users == result[0]:
                result[1] = max(result[1], total_purchase)
            return
        for d in discount:
            emo_rate.append(d)
            dfs(order + 1)
            emo_rate.pop()

    # 정해진 할인 비율대로 가격을 할인해 총 구입 가격을 계산하는 함수
    def calcul(emo_rate):
        plus_users = 0
        total_purchase = 0
        for user in users:
            purchase = 0
            discount_rate, limit = user[0], user[1]
            for i in range(len(emo_rate)):
                rate = emo_rate[i]
                if rate >= discount_rate:
                    purchase += emoticons[i] * (100 - rate) / 100
            # 플러스 요금제 가입 여부 확인
            if purchase >= limit:
                plus_users += 1
            else:
                total_purchase += purchase

        return plus_users, total_purchase

    emo_rate = []
    result = [0, 0]
    dfs(0)

    return result