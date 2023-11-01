def solution(arr):
    def encode(y, x, l):
        # l == 1이면 어차피 아래 반복문에서 처리됨
        bef = arr[y][x]     # 최초 번호, 다른 수는 최초 번호와 무조건 같아야함.
        for i in range(y, y + l):
            for j in range(x, x + l):
                if arr[i][j] != bef:        # 다르면 쿼드트리
                    encode(y, x, l // 2)
                    encode(y, x + l // 2, l // 2)
                    encode(y + l // 2, x, l // 2)
                    encode(y + l // 2, x + l // 2, l // 2)
                    return
        else:
            answer[bef] += 1
        
        
    answer = [0, 0]
    encode(0, 0, len(arr))
    
    return answer