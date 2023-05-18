import sys

input = sys.stdin.readline

S = input().rstrip()

bracket_cnt = []
target = ""
cnt = 0

left, right = S.count("("), S.count(")")
if left + 2 == right:
    target = ")"  # )를  ( 로 바꿔야 함
    limit = 2     # 2까지는 괜찮아
elif left == right + 2:
    target = "("  # ( 를 ) 로 바꿔야 함
    limit = -2    # -2까지는 괜찮아
else:
    print(0)
    exit(0)

left_b, right_b = 0, 0
for i in range(len(S)):
    if left_b < right_b:             # 아직 괄호를 변경하지 않았을 때 변경하더라도 소용이 없음
        break
    if right_b - left_b > limit:     # 괄호를 이미 변경한 경우를 가정했을 때 아직 유효한지 검사
        cnt = 0
    if S[i] == target:
        cnt += 1

    if S[i] == "(":
        left_b += 1
    else:
        right_b += 1


print(cnt)
