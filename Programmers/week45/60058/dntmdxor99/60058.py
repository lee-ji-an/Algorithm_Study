def solution(p):
    if not p : 
        return p

    check, count = True, 0
    for i in range(len(p)):
        if p[i] == '(': 
            count += 1
        else: 
            count -= 1
            
        if count < 0:       # 닫는 괄호가 더 많으면, 이때부턴 올바른 괄호 문자열이 아님
            check = False       # 올바른 괄호 문자열이 아님
            
        elif count == 0:        # 균형잡힌 괄호 문자열임
            if check:       # 올바른 괄호 문자열이라면
                return p[: i + 1] + solution(p[i + 1 :])
            else:       # 올바른 괄호 문자가 아니라면
                temp = '(' + solution(p[i + 1 : ]) + ')'
                for char in p[1 : i]:
                    temp += '(' if char == ')' else ')'
                return temp