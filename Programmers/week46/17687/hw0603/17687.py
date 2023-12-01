from itertools import product
import math

def solution(n, t, m, p):
    # 숫자를 '0' ~ 'F'로 변환하는 딕셔너리
    convert = {i: str(i) for i in range(10)}
    convert.update({i+10: chr(65+i) for i in range(6)})
    
    arr = []
    l = math.ceil(math.log(t*m, n))  # 대략 (참여인원*구할 숫자 개수) 까지만 보면 됨. n진법에서 해당수의 자릿수 구하기
    
    # n진법에서 l자리의 수를 모두 구하고, 
    for cnt, prod in enumerate(product(range(n), repeat=l)):
        if (cnt > t*m):
            # (참여인원*숫자개수) 이상의 수를 계산하면 루프 탈출
            # 숫자는 최소 한자리이므로.. 모두 한 자리더라도 t*m까지 계산하면 t개의 숫자를 미리 계산 가능
            break
        digits = [convert[d] for d in prod]
        # Leading zero 삭제 후 arr에 추가
        zeroIdx = 0
        while (digits[zeroIdx] == '0' and zeroIdx+1 < len(digits)):
            zeroIdx += 1
        digits = digits[zeroIdx:]
        arr += digits
    
    # 순서에 맞는 제네레이터 정의하고 t개만큼만 answer에 추가
    gen = (i for idx, i in enumerate(arr) if idx % m == p-1)
    answer = ""
    while (len(answer) < t):
        answer += next(gen)
        
    return answer