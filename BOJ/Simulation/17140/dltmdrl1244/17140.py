from collections import Counter
r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(3)]
ans = 0

def operation():
    part_max = 0
    for i in range(len(arr)):
        dic = {}
        tmp = [j for j in arr[i] if j != 0]
        tmp = Counter(tmp).most_common()
        res = []
        
        tmp.sort(key = lambda x: (x[1], x[0]))
        for t in tmp:
            res += t
            
        if len(res) > 100:
            res = res[:100]
            
        arr[i] = res
        part_max = max(part_max, len(res))
    for j in range(len(arr)):
        arr[j] += [0] * (part_max - len(arr[j]))
        

for i in range(101):
    # out of range 에러 발생할 수 있으므로 try except 구문으로 묶어 준다
    try:
        if arr[r - 1][c - 1] == k:
            print(i)
            break
    except: pass
    
    if len(arr) < len(arr[0]):
        # list(zip(*arr)) 하면 행/열을 반전시킨 2차원 배열을 얻을 수 있다.
        arr = list(zip(*arr))
        operation()
        arr = list(zip(*arr))
    else:
        operation()
else:
    print(-1)