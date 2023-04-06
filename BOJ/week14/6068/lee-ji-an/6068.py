N = int(input())

time_table = []

for i in range(N):
    work_size, end_time = map(int, input().split())
    time_table.append((end_time, work_size))

time_table = sorted(time_table, reverse=True)

time_ptr = time_table[0][0]
for end_time, work_size in time_table:
    if time_ptr > end_time:
        time_ptr = end_time - work_size
    else:
        time_ptr -= work_size

if time_ptr < 0:
    print(-1)
else:
    print(time_ptr)
