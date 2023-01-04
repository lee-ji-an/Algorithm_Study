n = int(input())
sign = list(input().split())

maxans = float('-inf')
minans = float('inf')
M = []
m = []

def permutation():
    used = [0 for _ in range(10)]

    def generate(chosen, used, depth):
        global maxans, minans, M, m

        if depth == n + 1:
            ans = int(''.join(map(str, chosen)))
            if maxans < ans:
                M = chosen[:]
            if minans > ans:
                m = chosen[:]
            maxans = max(maxans, ans)
            minans = min(minans, ans)
            return

        for i in range(10):
            if not used[i]:
                if len(chosen) == 0 or (sign[depth-1] == '<' and chosen[-1] < i) or (sign[depth-1] == '>' and chosen[-1] > i):
                    used[i] = 1
                    generate(chosen+[i], used, depth + 1)
                    used[i] = 0

    generate([], used, 0)
    print(*M, sep="")
    print(*m, sep="")

permutation()