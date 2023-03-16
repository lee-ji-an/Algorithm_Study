import sys
input = sys.stdin.readline

arr = []
people = 0
n = int(input())
for _ in range(n):
    home, num = map(int,input().split())
    arr.append([home, num])
    people += num

arr.sort(key = lambda x: x[0])

count = 0
for home in arr:
    count += home[1]
    if count >= people / 2:
        print(home[0])
        break