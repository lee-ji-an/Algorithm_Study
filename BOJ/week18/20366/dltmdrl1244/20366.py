import sys
from itertools import combinations
input = sys.stdin.readline

def check_complex(complexes):
    for i in range(len(complexes)):
        for j in range(i+1, len(complexes)):
            if complexes[i].imag != complexes[j].imag and complexes[i].real != complexes[j].real and complexes[i].real != complexes[j].imag and complexes[i].imag != complexes[j].real:
                return True
    
    return False

def check_complexes(complex1, complex2):
    for c1 in complex1:
        for c2 in complex2:
            if c1.imag != c2.imag and c1.real != c2.real and c1.imag != c2.real and c1.real != c2.imag:
                return True
    
    return False

n = int(input())
snowballs = list(map(int, input().split()))
snowballs.sort()
answer = sys.maxsize

dic = dict()
height_list = []

for head, body in combinations([i for i in range(n)], 2):
    height = snowballs[head] + snowballs[body]
    height_list.append(height)
    if height in dic:
        dic[height].append(complex(head, body))
    else:
        dic[height] = [complex(head, body)]

height_list = list(set(height_list))
height_list.sort()

for i in range(0, len(height_list)):
    t = dic[height_list[i]]
    if len(t) >= 2:
        if check_complex(t):
            print(0)
            exit()

    for j in range(i-1, -1, -1):
        if check_complexes(dic[height_list[i]], dic[height_list[j]]):
            answer = min(answer, abs(height_list[i] - height_list[j]))
            break
    
    for j in range(i+1, len(height_list)):
        if check_complexes(dic[height_list[i]], dic[height_list[j]]):
            answer = min(answer, abs(height_list[i] - height_list[j]))
            break

print(answer)