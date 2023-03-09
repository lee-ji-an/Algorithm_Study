## Info
[2580 스도쿠](https://www.acmicpc.net/problem/2580)

## 💡 풀이 방법 요약
비트 마스킹과 백트래킹을 이용하여 풀이한다.  
스도쿠에서 관심 있는 정보는 가로, 세로, 3x3 구역 정보이므로 이들 세 가지 정보에 대해 각각 9개의 비트 마스크를 따로 관리해 주며, 구역 정보는 `(row//3)*3 + (col//3)` 과 같이 구한다.  
  
데이터를 입력 받으며 빈 칸에 대한 정보는 `(row, col, div)`의 튜플로 관리하며, `empty_slot`이라는 리스트에 모두 저장해 둔다.  
빈 칸이 아닐 경우에는 해당 위치의 비트 마스크에 비트를 마킹한다.
  
`solve(idx: int)` 함수는 `empty_slot`의 끝까지 탐색을 마쳤을 때 메인으로 리턴하며, 그 전까지는 재귀적 백트래킹을 수행한다.  
```python
def solve(idx: int):
    # empty_slot의 끝까지 탐색을 마쳤을 때 종료
    ...
    
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
            
            # solve(idx+1)가 리턴했다는 뜻은 1~9 중 들어갈 수 있는 숫자를 못 찾은 것이므로
            # 다시 빈 칸으로 만들고 마스크 삭제
            matrix[x][y] = 0
            div_mask[div] &= (~mask)
            row_mask[x] &= (~mask)
            col_mask[y] &= (~mask)
```
말로 설명하는 것 보다 코드를 그대로 적는 것이 더 이해가 빠를 것 같은 몇 안 되는 문제라 코드를 그대로 가져 왔다.

## 🙂 마무리
PyPy3으로는 6등 했는데 같은 코드로 Python3 제출하면 시간 초과가 뜬다;;
