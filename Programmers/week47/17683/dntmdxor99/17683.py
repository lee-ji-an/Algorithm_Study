def solution(m, musicinfos):
    mappings = {
        'A#' : 'H', 'C#' : 'I', 'D#' : 'J', 'F#' : 'K', 'G#' : 'L'
    }
    
    def transform(music):       
        for v, k in mappings.items():
            music = music.replace(v, k)
        
        return music
    
        
    def getFullInfo(startTime, endTime, music):
        l = len(music)
        fullTime = (int(endTime[0:2]) - int(startTime[0:2])) * 60
        fullTime += int(endTime[3:5]) - int(startTime[3:5])
        fullMusic = music * (fullTime // l) + music[0:fullTime % l]
                             
        return fullTime, fullMusic
    
    
    answer = ''
    answerT = 0
    m = transform(m)
    
    for mi in musicinfos:
        startTime, endTime, name, music = mi.split(',')
        music = transform(music)
        fullTime, fullMusic = getFullInfo(startTime, endTime, music)
        
        if m in fullMusic:
            if answerT < fullTime:
                answerT = fullTime
                answer = name
        
    return answer if answer else "(None)"