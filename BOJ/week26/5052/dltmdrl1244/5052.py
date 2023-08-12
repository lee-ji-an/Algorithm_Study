import sys
input = sys.stdin.readline


def solve(strings):
    for i in range(t-1):
        if strings[i+1][:len(strings[i])] == strings[i]:
            return "NO"
    
    return "YES"


for _ in range(int(input())):
    t = int(input())
    strings = [input().rstrip() for _ in range(t)]

    strings.sort()
    print(solve(strings))