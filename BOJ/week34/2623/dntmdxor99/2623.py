import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(m)]
    dq = deque()
    ans = []

    degree = [0] * (n + 1)
    sub_seq = [set() for _ in range(n + 1)]

    for seq in maps:
        for i in range(2, len(seq)):
            if seq[i] not in sub_seq[seq[i - 1]]:       # 중복처리
                degree[seq[i]] += 1     # 단계 추가
                sub_seq[seq[i - 1]].add(seq[i])     # 후순위 가수

    for i in range(1, n + 1):
        if degree[i] == 0:      # 제일 앞순위 가수
            dq.append(i)
    
    while dq:
        item = dq.popleft()
        ans.append(item)
        for i in sub_seq[item]:     # 후순위 가수들
            degree[i] -= 1
            if degree[i] == 0:      # 조건이 충족하면 덱에 넣음
                dq.append(i)    
            
    if len(ans) == n:   print(*ans, sep='\n')
    else:               print(0)