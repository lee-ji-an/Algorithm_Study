import sys
input = sys.stdin.readline

S = input().rstrip()
s_list = S.split(":")
group_list = []


def get_full_group(group):
    if len(group) < 4:
        return "0" * (4-len(group)) + group
    return group


flag = False
for i in range(0, len(s_list)):
    if flag:
        flag = False
        continue
    if s_list[i] == '':
        if s_list[i + 1] == '':  # 맨 처음 or 맨 끝에 :: 이 나왔을 경우
            omit_cnt = 8 - (len(s_list)-2)
            flag = True
            i += 1
        else:
            omit_cnt = 8 - (len(s_list)-1)

        for j in range(i, i+omit_cnt):
            group_list.append("0000")
        continue
    group_list.append(get_full_group(s_list[i]))

print(":".join(group_list))
