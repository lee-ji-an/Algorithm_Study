from collections import deque

def solution(name):
    calc = lambda x: min(abs(ord(x) - ord('A')), 26-abs(ord(x) - ord('A')))
    visitedSet = set(i for i in range(len(name)) if name[i] == 'A')
    visitedSet.add(0)  # 첫 인덱스는 커서 이동 없이 바로 조작 가능

    answer = sum(map(calc, list(name)))  # 이동 횟수를 제외한 순수 문자 조작 횟수
    
    q = deque([(0, visitedSet, 0)])  # pos, hist, cnt
    length = len(name)
    while (q):
        pos, hist, cnt = q.popleft()
        if (len(hist) == length):
            answer += cnt  # 커서 이동을 위한 횟수
            break
        
        for k in (-1, +1):
            nPos = (pos + k) % length
            q.append((nPos, hist.union({nPos}), cnt+1))
    
    return answer

print(solution("JEROEN"))