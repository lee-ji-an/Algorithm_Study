import sys

inputs = sys.stdin.readline

flag = True
n = int(inputs())
s = []
dict = {}
for i in range(n):
    s.append(inputs().strip())
    for j in range(len(s[i])):
        if not dict.get(s[i][j]):
            dict[s[i][j]] = pow(10, len(s[i]) - j - 1)
        else:
            dict[s[i][j]] += pow(10, len(s[i]) - j - 1)

alphaNum = len(dict)
visited = [0] * 10
number = [i for i in range(9, 9 - alphaNum, -1)]
keys = list(dict.keys())
alphaList = sorted(list(dict.items()), key=lambda x: x[1])
alphaList.reverse()
alphaDict = {}
temp = 9
for item in alphaList:
    alphaDict[item[0]] = temp
    temp -= 1
maxRes = 0
result = 0
for word in s:
    num = 0
    for i in range(len(word)):
        num *= 10
        num += alphaDict[word[i]]
    result += num
print(result)
