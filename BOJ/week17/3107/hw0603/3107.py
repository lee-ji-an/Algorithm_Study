import sys 

addr = sys.stdin.readline().strip().split(':')

# ::1 같은 주소의 경우 빈 원소('')가 존재하므로 처리
if ('' in addr):
    while (len(addr) > 8):
        addr.pop(addr.index(''))
    while (len(addr) < 8):
        addr.insert(addr.index(''), '0000')

for i in range(8):
    if (len(addr[i]) < 4):  # 4자리가 아니면 앞에 0을 붙여줌
        addr[i] = addr[i].zfill(4)

print(*addr, sep=':')
