from itertools import product

def simulate(users, emo, tc) -> tuple:
    subscriber, sales = 0, 0
    getprice = lambda idx: emo[idx]*(100-tc[idx])/100  # 할인가
    
    for percentage, budget in users:
        if ((totalprice := sum(getprice(i) for i in range(len(emo)) if tc[i] >= percentage)) >= budget):
            subscriber += 1
        else:
            sales += totalprice

    return (subscriber, sales)

def solution(users, emoticons):
    return max(
        simulate(users, emoticons, tc) for tc in product((10, 20, 30, 40), repeat=len(emoticons))
    )