import sys
sys.setrecursionlimit(10**8)

def solution(arr):
    answer = []
    
    def checkAllSame(a, b, c, d) -> bool:
        lastFound = None
        for i in range(a, c):
            for j in range(b, d):
                if ((lastFound is not None) and lastFound != arr[i][j]):
                    return False
                lastFound = arr[i][j]
        return True
    
    def recur(a, b, c, d) -> list:
        cntData = [0, 0]
        # 전달받은 범위가 모두 같은 데이터면 더 깊이 내려가지 않음
        if (checkAllSame(a, b, c, d)):
            cntData[arr[a][b]] += 1
            return cntData
        # 전달받은 범위에 다른 데이터가 섞여 있으면 4분할 후 아래 가지에 계산 위임
        dt = []
        dt.append(recur(a, b, (a+c)//2, (b+d)//2))
        dt.append(recur(a, (b+d)//2, (a+c)//2, d))
        dt.append(recur((a+c)//2, b, c, (b+d)//2))
        dt.append(recur((a+c)//2, (b+d)//2, c, d))
        
        for cnt0, cnt1 in dt:
            cntData[0] += cnt0
            cntData[1] += cnt1
        
        return cntData
    
    answer = recur(0, 0, len(arr), len(arr[0]))
    
    return answer
