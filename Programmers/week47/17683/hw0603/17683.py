from itertools import cycle

# 반음을 문자 하나로 치환
def convert(melody):
    return melody.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

def solution(m, musicinfos):
    answer = "(None)"
    maxDuration = 0
    m = convert(m)
    
    for start, end, title, sheet in map(lambda x: x.split(','), musicinfos):
        # 시간정보 파싱
        start = tuple(map(int, start.split(':')))
        end = tuple(map(int, end.split(':')))
        duration = (end[0]-start[0])*60 + (end[1]-start[1])  # 시*60 + 분
        
        sheet_cycle = cycle(convert(sheet))  # 무한 이터레이터
        sheet = ""
        while (len(sheet) < duration):
            sheet += next(sheet_cycle)
        
        if (duration > maxDuration and m in sheet):
            maxDuration, answer = duration, title
    
    return answer
