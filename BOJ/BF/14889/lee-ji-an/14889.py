import sys


def calcul(team):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += scoreTable[team[i]][team[j]]
            score += scoreTable[team[j]][team[i]]
    return score


def combination(start, depth):
    global linkScore, startScore, minRes
    if depth == n//2:
        teamRes2 = []
        for item in member:
            if item not in teamRes:
                teamRes2.append(item)
        linkScore = calcul(teamRes)
        startScore = calcul(teamRes2)
        if minRes > abs(linkScore-startScore):
            minRes = abs(linkScore-startScore)
        return
    for idx in range(start, n):
        teamRes[depth] = member[idx]
        combination(idx+1, depth+1)

inputs = sys.stdin.readline
n = int(inputs())
scoreTable = []
linkScore = 0
startScore = 0
minRes = float('inf')
for i in range(n):
    scoreTable.append(list(map(int, inputs().split())))
teamRes = [-1] * (n//2)
member = [i for i in range(n)]
combination(0, 0)
print(minRes)