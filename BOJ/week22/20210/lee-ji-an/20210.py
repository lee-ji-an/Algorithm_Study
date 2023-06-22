import sys
from functools import cmp_to_key

input = sys.stdin.readline

N = int(input())

file_names = []
ch_dict = {}
for i in range(N):
    file_names.append(input().rstrip())

for i in range(65, 91):  # A~Z
    ch_dict[i] = (i - 65)*2
for i in range(97, 123):  # a~z
    ch_dict[i] = (i - 97)*2 + 1


# 숫자, 영어를 분리
def split_word(word):
    w = list(word)
    split_list = []
    flag = w[0].isdigit()
    string = ""
    for i in range(len(w)):
        if w[i].isdigit() == flag:
            string = string + w[i]
        else:
            split_list.append(string)
            string = w[i]
            flag = not flag
    split_list.append(string)
    return split_list


def operate(v1, v2):
    if v1 <= v2:
        return -1
    else:
        return 1


def compare(w1, w2):
    w1_split, w2_split = split_word(w1), split_word(w2)
    for i in range(min(len(w1_split), len(w2_split))):
        if w1_split[i] == w2_split[i]:
            continue
        if w1_split[i].isdigit() and not w2_split[i].isdigit():  # T, F
            return -1
        elif w1_split[i].isdigit() and w2_split[i].isdigit():  # T, T
            num1, num2 = int(w1_split[i]), int(w2_split[i])
            if num1 == num2:  # 숫자 크기가 같을 때, 길이를 비교
                return operate(len(w1_split[i]), len(w2_split[i]))
            else:
                return operate(num1, num2)
        elif not w1_split[i].isdigit() and w2_split[i].isdigit():  # F, T
            return 1
        else:  # F, F
            for j in range(min(len(w1_split[i]), len(w2_split[i]))):
                if w1_split[i][j] != w2_split[i][j]:
                    return operate(ch_dict[ord(w1_split[i][j])], ch_dict[ord(w2_split[i][j])])
            # 한 단어가 다른 단어에 포함될 때, 길이를 비교
            return operate(len(w1_split[i]), len(w2_split[i]))
    # 문자열 전체게 다른 문자열에 포함될 때
    return operate(len(w1), len(w2))


print(*sorted(file_names, key=cmp_to_key(compare)), sep='\n')
