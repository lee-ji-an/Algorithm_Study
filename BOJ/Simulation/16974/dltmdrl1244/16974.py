n, x = map(int, input().split())
size = [1]
patty = [1]

for i in range(50):
    size.append(size[-1] * 2 + 3)
    patty.append(patty[-1] * 2 + 1)

def recur(i, k):
    if k == 0:
        return 0
    
    if k == size[i]:
        return patty[i]
    
    elif k == size[i] // 2 + 1:
        return patty[i-1] + 1
    
    elif k < size[i] // 2 + 1:
        return recur(i-1, k-1)
    
    else:
        return patty[i-1] + 1 + recur(i-1, k - (size[i-1] + 2))

print(recur(n, x))