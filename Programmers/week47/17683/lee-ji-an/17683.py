def solution(m, musicinfos):
    # 반올림 음은 소문자 알파벳으로 변경
    def change(music):
        if 'A#' in music:
            music = music.replace('A#', 'a')
        if 'F#' in music:
            music = music.replace('F#', 'f')
        if 'C#' in music:
            music = music.replace('C#', 'c')
        if 'G#' in music:
            music = music.replace('G#', 'g')
        if 'D#' in music:
            music = music.replace('D#', 'd')

        return music

    answer = "(None)"
    max_time = 0
    changed_m = change(m)
    for info in musicinfos:
        info_list = info.split(',')

        # 재생 시간 구하기
        start_h, start_m = map(int, info_list[0].split(':'))
        end_h, end_m = map(int, info_list[1].split(':'))
        play_time = (end_h * 60 + end_m) - (start_h * 60 + start_m)

        # 반올림 음은 소문자로 변경 -> 전체 재생 시간 동안의 멜로디 만들어서 저장
        melody = change(info_list[3])
        music_str = (play_time // len(melody)) * melody + melody[0: play_time % len(melody)]

        # m과 멜로디가 일치하고 재생 시간이 가장 긴지 확인
        if changed_m in music_str and play_time > max_time:
            answer = info_list[2]
            max_time = play_time

    return answer
