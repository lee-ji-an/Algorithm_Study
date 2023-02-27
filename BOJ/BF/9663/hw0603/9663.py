import sys

N = int(sys.stdin.readline())
cnt = 0

# Q[i] = i번째 row에는 몇 번째 col에 Queen이 존재하는가?
def nqueen_bt(Q: list):
    global cnt
    r = len(Q)
    if (r >= N):
        cnt += 1
        return
    
    for j in range(N):
        legal = True
        for i in range(r):
            if (Q[i] == j or Q[i] == j+r-i or Q[i] == j-r+i):
                legal = False
                break
        
        if (legal):
            Q.append(j)
            nqueen_bt(Q)
            Q.pop()

nqueen_bt([])
print(cnt)
