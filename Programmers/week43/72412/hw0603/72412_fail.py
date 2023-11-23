def solution(info, query):
    def search(lang, part, exp, food, score):        
        bitmask = 0
        if (lang):
            bitmask += 0b_00_00_00_11
        if (part):
            bitmask += 0b_00_00_11_00
        if (exp):
            bitmask += 0b_00_11_00_00
        if (food):
            bitmask += 0b_11_00_00_00
        
        queryInfo = sum(bitData.get(key, 0) for key in (lang, part, exp, food))
        
        cnt = 0
        for devInfo, testScore in db:
            devInfo &= bitmask
            if (queryInfo == devInfo and testScore >= score):
                cnt += 1
        return cnt
            
    
    answer = []
    
    bitData = {
        "cpp": 1, "java": 2, "python": 3,
        "backend": 4, "frontend": 8,
        "junior": 16, "senior": 32,
        "chicken": 64, "pizza": 128
    }
    db = []
    
    # 데이터 삽입
    for dev in map(str.split, info):
        devInfo = sum(bitData.get(key, 0) for key in dev)
        testScore = int(dev[-1])
        db.append((devInfo, testScore))
        
    # 검색
    for q in map(lambda x: x.replace("and", '').split(), query):
        res = search(*tuple(map(lambda x: None if x == '-' else x, q[:-1])), int(q[-1]))
        answer.append(res)

    return answer