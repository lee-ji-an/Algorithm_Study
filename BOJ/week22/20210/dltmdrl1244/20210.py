import sys
import heapq
input = sys.stdin.readline

'''
알파벳끼리는 AaBb ... 의 대소관계를 가짐 (A가 가장 작음)
모든 숫자는 알파벳보다 작음
숫자들끼리는 작은 숫자가 작음
같은 값의 숫자라면 앞의 0이 적은 것이 작음 (12 < 00012)
'''

def make_tuple(word):
    result = []
    t = 0
    numlen = 0

    for w in word:
        # 문자
        if 65 <= ord(w) <= 90 or 97 <= ord(w) <= 122:
            if numlen:
                result.append((1, t, numlen))
                t = 0
                numlen = 0
            result.append((2, (ord(w) - 65) * 2) if 65 <= ord(w) <= 90 else (2, (ord(w) - 97) * 2 + 1))

        # 숫자
        else:
            t *= 10
            t += int(w)
            numlen += 1
    
    # 남아 있는 숫자가 있을 경우 (문자열이 숫자로 끝났을 경우) 나머지 처리
    if numlen:
        result.append((1, t, numlen))
    
    return tuple(result)

def restore_tuple(word):
    # 튜플 형태로 저장된 값을 다시 문자열로 원상복구
    result = ""

    for tup in word:
        if tup[0] == 1: # 숫자
            result += str(tup[1]).zfill(tup[2])
        else: # 문자
            if tup[1] % 2: # 홀수 => 소문자.
                result += chr(int((tup[1] - 1) / 2) + 97)
            else:
                result += chr(int(tup[1] / 2) + 65)
    
    return result
            

n = int(input())
words = []
heap = []

for _ in range(n):
    heapq.heappush(heap, make_tuple(input().rstrip()))

for _ in range(n):
    print(restore_tuple(heapq.heappop(heap)))
