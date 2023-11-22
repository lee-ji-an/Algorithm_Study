def solution(msg):
    answer = []
    word_dict = {}
    word_dict_idx = 27
    idx = 0
    while idx < len(msg):
        # idx 지점에서 시작하는 문자열 중 사전에 있는 가장 긴 문자열 찾기
        # word : idx 지점에서 일치하는 가장 긴 문자열을 저장
        word = msg[idx]
        for i in range(idx + 1, len(msg)):
            if word + msg[i] in word_dict:
                word += msg[i]
            else:
                break

        # 사전에 등록된 단어 번호를 정답 배열에 추가
        # 사전에 있는 최장 문자열의 길이가 1이라면 아스키코드로 해결
        if len(word) == 1:
            answer.append(ord(word) - ord('A') + 1)
        else:
            answer.append(word_dict[word])

        # 사전에 단어 등록하기
        if idx + len(word) < len(msg):
            word_dict[word + msg[idx + len(word)]] = word_dict_idx
            word_dict_idx += 1

        # 다음에 탐색할 단어 위치로 이동
        idx += len(word)

    return answer
