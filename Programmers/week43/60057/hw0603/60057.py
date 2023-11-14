def solution(s):
    answer = len(s)
    
    for unitLen in range(1, len(s)//2 + 1):
        testStr = ""
        idx = 0
        while (idx < len(s)):
            unitStr = s[idx:idx+unitLen]  # 단위길이만큼 문자열 잘라서 저장
            unitFreq = 1

            # 잘린 문자열이 매치되지 않을 때 까지 idx와 unitFreq 증가
            while (unitStr == s[idx+unitLen:idx+unitLen+unitLen]):
                idx += unitLen
                unitFreq += 1
            
            # unitStr이 2회 이상 등장한 경우 횟수를 기록하여 압축
            testStr += f"{unitFreq if unitFreq >= 2 else ''}{unitStr}"
            idx += unitLen  # 단위길이만큼 인덱스 점프
            
        answer = min(answer, len(testStr))

    return answer
