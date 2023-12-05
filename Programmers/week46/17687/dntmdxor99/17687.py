hex = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 
      6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'A', 11 : 'B',
      12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}       # 16진수 변환용


def solution(n, t, m, p):
    def createNotation(n, l):
        notation = '01'     # 최소 l은 2이므로
        for i in range(2, l + 1):
            temp = ''
            while i != 0:
                temp += f'{hex[i % n]}'     # 각 자리를 넣음
                i = i // n

            notation += temp[::-1]
            if len(notation) >= l:      # 길이가 l이상이면 뒤는 더 이상 알아볼 필요가 없음.
                return notation
        
        return notation
            
        
    notation = createNotation(n, t * m)     # 최대 길이는 t * m임
    answer = notation[p - 1 : t * m : m]    # p번째부터 m씩 건너뛰면서 t개를 가져옴
    return answer