import sys


def combination(depth, start, spells):
    if depth == k:
        combi.append(spells)
        return
    for i in range(start, len(alphalist)):
        combination(depth + 1, i + 1, spells | (1 << (ord(alphalist[i]) - ord('a'))))


inputs = sys.stdin.readline
n, k = map(int, inputs().split())
k -= 5
words = []

spell = [0 for i in range(n)]
totalSpell = 0
maxCnt = 0
for i in range(n):
    words.append(inputs().strip())
combi = []
bitstring = 0
alphalist = []
binlist = []
for i in range(n):
    bitstring = 0
    for j in range(len(words[i])):
        if words[i][j] not in ['a', 'n', 't', 'i', 'c']:
            if words[i][j] not in alphalist:
                alphalist.append(words[i][j])
            bitstring = (1 << (ord(words[i][j]) - ord('a')) | bitstring)
    binlist.append(bitstring)
for i in range(n):
    totalSpell = totalSpell | binlist[i]

temp = 0
if len(alphalist) > k:
    combination(0, 0, 0)
else:
    for i in range(len(alphalist)):
        temp = temp | (1 << (ord(alphalist[i])-ord('a')))
    combi = [temp]
for i in range(len(combi)):
    cnt = 0
    for b in binlist:
        if b & combi[i] == b:
            cnt += 1
    if maxCnt < cnt:
        maxCnt = cnt
print(maxCnt)