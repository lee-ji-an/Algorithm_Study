def isValid(string):
    stack = []
    for ch in string:
        if (ch == '('):
            stack.append(ch)
        else:
            if not (stack):
                return False
            stack.pop()
    return len(stack) == 0

def split(p):
    cnt = [0, 0]
    u = ''
    for ch in p:
        if (ch == '('):
            cnt[0] += 1
        else:
            cnt[1] += 1
        u += ch
        if (cnt[0] == cnt[1]):
            break
    v = p[len(u):]
    return u, v

def process(u):
    newU = ''
    for idx, ch in enumerate(u):
        if (idx in {0, len(u)-1}):
            continue
        newU += '(' if ch == ')' else ')'
    
    return newU

def solution(p):
    if (isValid(p)):
        return p

    u, v = split(p)
    if (isValid(u)):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + process(u)
