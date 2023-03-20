import sys
input = sys.stdin.readline

N = int(input())
num_list = [[0] * N for _ in range(4)]
ab_dict = {}
ans = 0


for i in range(N):
    row = list(map(int, input().split()))
    for j in range(4):
        num_list[j][i] = row[j]

for i in range(N):  # A, B 리스트 합을 key 로 가지는 딕셔너리를 저장
    for j in range(N):
        num = num_list[0][i] + num_list[1][j]
        if num in ab_dict:
            ab_dict[num] += 1
        else:
            ab_dict[num] = 1

for i in range(N):
    for j in range(N):
        num = num_list[2][i] + num_list[3][j]  # C, D 리스트를 에 있는 값의 합을 구해서 딕셔너리 탐색
        if -num in ab_dict.keys():
            ans += ab_dict[-num]

print(ans)
