from itertools import permutations
import re


def calculate(operends, operators, priority):
    for target in priority:
        for idx, op in enumerate(operators):
            if (op == target):
                adjNumIdx = idx+1
                while (operends[adjNumIdx] == ''):
                    adjNumIdx += 1
                value = eval(f"{operends[idx]}{op}{operends[adjNumIdx]}")
                operends[adjNumIdx] = value
                operends[idx] = operators[idx] = ''  # 계산한 식 마킹

    return operends[-1]


def solution(expression):
    # 연산자, 피연산자 분리
    pattern = re.compile(r'[0-9]+')
    operends = list(map(int, pattern.findall(expression)))
    operators = pattern.split(expression)[1:-1]

    uniqueOp = list(set(operators))
    
    answer = max(
        abs(calculate(operends[:], operators[:], priority))
            for priority in permutations(uniqueOp, len(uniqueOp))
    )

    return answer