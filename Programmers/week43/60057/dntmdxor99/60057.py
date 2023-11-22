def solution(s):
    l = len(s)
    answer = l
    
    for i in range(1, l // 2 + 1):      # 단위는 1부터 최대 절반까지임
        subStr, idx = "", 0
        while idx < l:      # 범위를 벗어나면 안 됨
            token, cnt = s[idx : idx + i], 1        # 압축할 문자열
            while token == s[idx + i : idx + i * 2]:        # 뒤의 문자열이 같다면
                idx, cnt = idx + i, cnt + 1
            
            # 문자열을 완성함
            subStr = subStr + (str(cnt) + token if cnt != 1 else token)
            idx = idx + i
        
        answer = min(len(subStr), answer)       # 길이 체크
    
    return answer