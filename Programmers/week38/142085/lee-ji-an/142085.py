def solution(n, k, enemy):
    import heapq

    cur_enemy = []
    total_enemy = 0

    answer = len(enemy)

    for i in range(len(enemy)):
        e = enemy[i]
        # 적군의 숫자가 더 많을 때
        if total_enemy + e > n:
            # 무적권이 남아있다면 사용
            if k > 0:
                if cur_enemy:
                    heapq.heappush(cur_enemy, -e)
                    total_enemy += e

                    m_enemy = heapq.heappop(cur_enemy) * (-1)
                    total_enemy -= m_enemy

                k -= 1
            # 무적권이 남아있지 않으면 종료
            else:
                answer = i
                break
        # 적군의 숫자가 더 적을 때
        else:
            heapq.heappush(cur_enemy, -e)
            total_enemy += e

    return answer
