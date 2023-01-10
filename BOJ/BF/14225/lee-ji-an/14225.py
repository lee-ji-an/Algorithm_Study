def dfs(idx, sum):
    global min
    if idx >= n:
        return
    sum = sum + s[idx]
    sum_list.append(sum)  # visited 리스트 추가해서 확인 가능
    # if sum == min + 1:
    #     min = sum
    dfs(idx+1, sum-s[idx])
    dfs(idx+1, sum)

n = int(input())
s = list(map(int, input().split()))
min = 0
sum_list = []
dfs(0, 0)
sum_list.sort()
for i in range(len(sum_list)):
    if sum_list[i] == min+1:
        min = min + 1

print(min+1)