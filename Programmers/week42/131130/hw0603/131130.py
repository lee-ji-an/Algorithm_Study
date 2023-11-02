def bit_count(num):
    if (num <= 5):
        return (0, 1, 2, 2, 3, 4)[num]  # "11011" 패턴에서 num에 따른 '1'의 합

    # 5^maxexp가 num을 넘지 않는 최대 승수 구함
    maxexp = 1
    while (5 ** (maxexp + 1) < num):
        maxexp += 1

    group = num // (5 ** maxexp)  # 패턴 중 몇번째 그룹까지 완전히 속하는가? (1-base)
    remainder = num % (5 ** maxexp)  # 11011 패턴에 속하지 않고 남는 나머지 개수

    # 3개 이상의 그룹에 속하는 경우, 3번째 그룹은 0...0 이므로 4^maxexp개를 하나 덜 더해줘야 함
    answer = (group if group < 3 else group-1) * (4 ** maxexp)
    
    # 2개의 그룹에 속하는 경우, 3번째 그룹은 모두 0이므로 더 계산할 필요 없음
    # 다른 모든 경우, 다음 그룹에 살짝 걸치는(remainder) 만큼의 1 개수를 더해줘야 함
    return answer + (0 if group == 2 else bit_count(remainder))
    

def solution(_, l, r):
    return bit_count(r) - bit_count(l-1)
