def solution(sequence, k):
    answer = []
    minimum = float('inf')
    l = len(sequence)
    
    left, right = 0, 0
    total = sequence[0]
    
    if total == k:      # 시작부터 조건을 만족한다면 그냥 반환하면 됨
        return [0, 0]
    else:
        while left <= right < l:
            if total < k:       # 목표보다 작다면 right를 옮김
                right += 1
                if right >= l:      # 범위를 벗어난다면 종료함
                    break
                total += sequence[right]
            elif total > k:     # 목표보다 크다면 left를 옮김
                total -= sequence[left]
                left += 1
            else:
                if right - left < minimum:      # 길이
                    minimum = right - left
                    answer = [left, right]
                    
                # 아래는 left, right를 모두 오른쪽으로 한 칸 옮김
                total -= sequence[left]
                left += 1
                right += 1
                if right >= l:
                    break    
                total += sequence[right]
    
    return answer