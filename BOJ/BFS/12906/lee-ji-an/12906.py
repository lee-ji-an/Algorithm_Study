import sys
from collections import deque

input = sys.stdin.readline


# a, b, c 막대의 초기 상태를 입력받아 bfs로 원판을 옮기는 경우를 탐색해서 목표 지점에 도달했을 때 옮긴 횟수를 반환하는 함수
def bfs(a_start, b_start, c_start, end_state):
    state_set = set()
    q = deque()
    disk_list = [0] * 4
    stock = [0] * 5
    q.append((0, a_start, b_start, c_start, 0))  # 어느 막대에 꽂았는지 표시 / prev, a 막대의 상태, b 막대의 상태, c 막대의 상태, cnt(옮긴 횟수)
    while q:
        prev, disk_list[1], disk_list[2], disk_list[3], cnt = q.popleft()
        for stick in range(1, 4):
            if prev == stick or disk_list[stick] <= 0:
                continue
            target_disk = 0b11 & disk_list[stick]  # 제일 위에 있는 원판을 저장
            minus = disk_list[stick] >> 2  # 막대에서 원판 빼기
            for target_stick in range(1, 4):
                if stick == target_stick:
                    continue
                # 큐에 저장할 튜플 생성
                plus = (disk_list[target_stick] << 2) + target_disk  # 원판 꽂기
                extra = tuple({A, B, C} - {stick, target_stick})[0]  # A, B, C 중 원판을 뺀 막대와 원판을 꽂은 막대가 아닌 나머지 막대를 저장
                stock[0] = target_stick
                stock[stick] = minus
                stock[target_stick] = plus
                stock[extra] = disk_list[extra]
                stock[4] = cnt + 1

                # state 집합에 현재 상태를 저장 -> 중복 체크
                state = get_state([stock[1], stock[2], stock[3]])
                if state == end_state:
                    return cnt + 1
                if state not in state_set:  # 상태 중복 체크
                    state_set.add(state)
                    q.append(tuple(stock))


# ABC 로 이루어진 string을 A-> 0b01 B-> 0b10 C-> 0b11 로 바꿔서 이진수로 반환하는 함수
def string_to_bit(disk_string):
    bit_num = 0
    for i in range(len(disk_string)):
        if disk_string[i] == 'A':
            bit_num = (bit_num << 2) + A
        elif disk_string[i] == 'B':
            bit_num = (bit_num << 2) + B
        else:
            bit_num = (bit_num << 2) + C

    return bit_num


# bit 가 몇 자리인지 계산하는 함수
def bit_digit(bit):
    digit = 0
    while bit != 0:
        digit += 1
        bit = bit >> 1

    return digit


# ABC 원판이 몇 개 있는지 리스트로 반환하는 합수
def count_disk_num():
    disk_num = [0, 0, 0, 0]
    for i in range(1, 4):
        for j in range(input_list[i][0]):
            last_disk = 0b11 & (input_list[i][1] >> j * 2)
            if last_disk == A:
                disk_num[A] += 1
            elif last_disk == B:
                disk_num[B] += 1
            else:
                disk_num[C] += 1

    return disk_num


# A, B, C 원판 비트 스트링을 연결해서 상태를 나타내는 하나의 비트스트링을 반환
def get_state(disk):
    state = disk[0]
    for i in range(1, 3):
        state = ((state << 3) << bit_digit(disk[i])) + disk[i]

    return state


A, B, C = 0b1, 0b10, 0b11
input_list = [0]
disk_num = [0, 0, 0, 0]
for i in range(1, 4):
    input_stick = input().split()
    for j in range(int(input_stick[0])):  # A, B, C 원판 갯수 세기
        if input_stick[1][j] == 'A':
            disk_num[A] += 1
        elif input_stick[1][j] == 'B':
            disk_num[B] += 1
        else:
            disk_num[C] += 1
    if len(input_stick) > 1:
        input_list.append((int(input_stick[0]), string_to_bit(input_stick[1])))
    else:
        input_list.append((int(input_stick[0]), 0))

answer = get_state([string_to_bit('A' * disk_num[A]), string_to_bit('B' * disk_num[B]), string_to_bit('C' * disk_num[C])])

if get_state([input_list[A][1], input_list[B][1], input_list[C][1]]) == answer:
    print(0)
else:
    print(bfs(input_list[1][1], input_list[2][1], input_list[3][1], answer))
