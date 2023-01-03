import itertools
import sys

K = int(sys.stdin.readline())
ineqs = sys.stdin.readline().rstrip().split(" ")

result = []
for pair in itertools.permutations([i for i in range(10)], K+1):
    flag = True
    for i in range(len(ineqs)):
        if (ineqs[i] == "<"):
            if (pair[i] < pair[i+1]):
                continue
            else:
                flag = False
                break
        else:
            if (pair[i] > pair[i+1]):
                continue
            else:
                flag = False
                break
    if (flag):
        result.append(pair)

print(''.join(map(str, list(max(result)))))
print(''.join(map(str, list(min(result)))))