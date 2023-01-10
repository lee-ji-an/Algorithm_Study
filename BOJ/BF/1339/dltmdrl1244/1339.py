n = int(input())
words = []
dic = {}
assign = [-1 for _ in range(10)]
ans = 0
for _ in range(n):
    words.append(list(input()))

for word in words:
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = pow(10, len(word)-i-1)
        else:
            dic[word[i]] += pow(10, len(word)-i-1)

mylist = list(dic.values())
mylist = sorted(mylist, reverse=True)

a = 9
for n in mylist:
    ans += n * a
    a -= 1

print(ans)

# for word in words:
#     while len(word) != 8:
#         word.insert(0, 0)
#
# a = 9
# for i in range(8):
#     for j in range(len(words)):
#         if type(words[j][i]) is str:
#             if words[j][i] not in assign:
#                 assign[a] = words[j][i]
#                 a -= 1
#             words[j][i] = assign.index(words[j][i])
#
# for word in words:
#     ans += int("".join(map(str, word)))
# print(ans)
# ========================================================================
# t = copy.deepcopy(words)
#
# def solve(chosen):
#     global answer
#     sum = 0
#     for i in range(len(words)):
#         for j in range(len(words[i])):
#             t[i][j] = chosen[dic.index(words[i][j])]
#
#     for word in t:
#         sum += int("".join(map(str, word)))
#
#     answer = max(answer, sum)
#     return
#
# def permutation(r):
#     used = [0 for _ in range(10)]
#     chosen = []
#     def generate(used, chosen, depth):
#         if depth == r:
#             # print(chosen)
#             solve(chosen)
#             return
#         for i in range(10):
#             if not used[i]:
#                 used[i] = 1
#                 generate(used, chosen+[i], depth + 1)
#                 used[i] = 0
#     generate(used, [], 0)
#
# permutation(len(dic))
#
# print(answer)