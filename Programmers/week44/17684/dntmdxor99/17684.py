def solution(msg):
    answer = []
    
    maps = {}
    idx = 1
    
    for i in range(26):
        maps[chr(i + 65)] = idx
        idx += 1
    
    l = len(msg)
    i = 0
    
    while i < l:
        subStr = msg[i]     # 초기값 설정
        subIdx = maps[msg[i]]       # 초기 번호 설정
        for j in range(i + 1, l):       # 하나씩 넣어봄
            subStr += msg[j]
            if subStr in maps:      # 있으면 다음으로 넘김
                subIdx = maps[subStr]
                i += 1
            else:
                break
        answer.append(subIdx)       # 번호 입력
        maps[subStr] = idx      # 새로운 번호 등록
        idx += 1
        i += 1
    
    return answer