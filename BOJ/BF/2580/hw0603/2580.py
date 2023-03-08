from collections import deque
import sys

matrix = [[0]*9 for _ in range(9)]  # 스도쿠 행렬
row_mask = [0] * 9  # 각 행에 대한 비트 마스크
col_mask = [0] * 9  # 각 열에 대한 비트 마스크
div_mask = [0] * 9  # 3x3 구역에 대한 비트 마스크
empty_slot = []  # 빈 칸의 좌표


# 백트래킹으로 스도쿠 풀이
def solve(idx: int):
    # empty_slot의 끝까지 탐색을 마쳤을 때 종료
    if (idx > len(empty_slot)-1):
        for i in range(9):
            print(*(matrix[i]))
        sys.exit()
    
    # 1~9까지 모두 넣어보기
    x, y, div = empty_slot[idx]
    available_bit = 0b1111111110 ^ (row_mask[x] | col_mask[y] | div_mask[div])  # 가용 비트 구함
    for num in range(1, 10):
        # 현재 빈 칸 위치에 num이 들어갈 수 있다면
        mask = (1 << num)
        if (available_bit & mask):
            # 스도쿠 행렬에 넣고
            matrix[x][y] = num
            # 비트 마스크 정보 업데이트
            row_mask[x] |= mask
            col_mask[y] |= mask
            div_mask[div] |= mask
            
            # 다음 빈칸에 대해 풀이
            solve(idx+1)
            
            # solve()가 리턴했다는 뜻은 1~9 중 들어갈 수 있는 숫자를 못 찾은 것이므로
            # 다시 빈 칸으로 만들고 마스크 삭제
            matrix[x][y] = 0
            div_mask[div] &= (~mask)
            row_mask[x] &= (~mask)
            col_mask[y] &= (~mask)


# 데이터 읽고 준비
for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    for j, num in enumerate(line):
        matrix[i][j] = num  # 스도쿠 행렬에 데이터 추가
        div = (i//3)*3 + (j//3)  # 3x3 구역 정보

        # 빈칸이면 리스트에 추가
        if (num == 0):
            empty_slot.append((i, j, div))
        # 빈 칸이 아니라면 비트 마스크 정보 업데이트
        else:
            row_mask[i] |= (1 << num)
            col_mask[j] |= (1 << num)
            div_mask[div] |= (1 << num)

# 0번째 빈 칸 부터 스도쿠 풀이 시작
solve(0)
