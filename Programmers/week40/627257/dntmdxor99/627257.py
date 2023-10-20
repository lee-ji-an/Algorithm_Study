import re
from itertools import permutations

def solution(expression):
    answer = 0
    
    equation = re.split('([-+*])', expression)
    equationOriginal = equation.copy()
    
    for priority in permutations(['-', '+', '*'], 3):
        for p in priority:
            i = 0
            while i < len(equation):        # 어차피 길이가 1이면 아래 문장 한 번만 실행하고 끝남
                if equation[i] == p:
                    equation[i - 1 : i + 2] = [str(eval(''.join(equation[i - 1 : i + 2])))]
                else:
                    i += 1
        answer = max(answer, abs(int(equation[0])))
        equation = equationOriginal.copy()

    return answer