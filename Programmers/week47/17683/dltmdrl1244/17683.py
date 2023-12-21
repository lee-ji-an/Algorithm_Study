def convertToMinute(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def convertToString(string):
    rv = ""
    for i in range(len(string)):
            if string[i] == '#':
                continue

            if string[i] in ('C', 'D', 'F', 'G', 'A'):
                if i != len(string) - 1 and string[i+1] == '#':
                    rv += chr(ord(string[i]) + 32)
                    continue

            rv += string[i]
    
    return rv
            
def solution(m, musicinfos):
    answer = []
    memory = convertToString(m)
    print(memory)
    
    
    for idx, music in enumerate(musicinfos):
        startTime, endTime, title, melody = music.split(",")
        startMin, endMin = convertToMinute(startTime), convertToMinute(endTime)
        duration = endMin - startMin
        melody = convertToString(melody)
        
        if len(melody) > duration:
            melody = melody[:duration]
        elif len(melody) < duration:
            while len(melody) < duration:
                melody += melody
            melody = melody[:duration]
        
        if memory in melody:
            answer.append((duration, idx, title))

    if answer:
        answer.sort(key = lambda x : (-x[0], x[1]))
        return answer[0][2]
    
    return "(None)"