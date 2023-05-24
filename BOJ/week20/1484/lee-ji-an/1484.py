import sys
input = sys.stdin.readline

G = int(input())

start_ptr = 1
end_ptr = 2
ans_list = []

# end_ptr: 현재 몸무게, start_ptr: 성원이가 기억하고 있던 몸무게
while end_ptr * end_ptr - (end_ptr - 1) * (end_ptr - 1) <= G:
    weight_value = end_ptr * end_ptr - start_ptr * start_ptr
    if weight_value < G:
        end_ptr += 1
    elif weight_value > G:
        start_ptr += 1
    else:
        ans_list.append(end_ptr)
        end_ptr += 1
        start_ptr += 1

if ans_list:
    for num in ans_list:
        print(num)
else:
    print(-1)
