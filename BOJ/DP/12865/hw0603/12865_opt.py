import sys

def knapsack():
    N, K = map(int, sys.stdin.readline().split())
    items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    items.sort(reverse=True)  # 무게가 높은 순으로 정렬
    bag = {0: 0}  # Key=가치, Value=무게

    for w_it, v_it in items:  # 각 물건들에 대해
        tmp = {}
        for v_bag, w_bag in bag.items():  # 지금 가방에 담긴 물건들에 대해 현재 조사대상 물건과 비교
            # 가방에 담긴 물건을 하나씩 빼 보면서 현재 물건을 넣는다고 가정.
            # 바꿔치기 후에 가방의 총 무게가 더 작아질 수 있다면
            if (w_sum := w_bag + w_it) <= bag.get(v_sum := v_bag + v_it, K):  # 가방에 현재 그 가치에 해당하는 무게정보가 없을 경우: 기본값=무게제한 K
                tmp[v_sum] = w_sum  # 해당 가치의 key에 무게 업데이트
        
        bag.update(tmp)

    return max(bag.keys())

print(knapsack())
