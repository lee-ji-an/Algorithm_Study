def solution(number, k):
    answer = []
    
    for n in number:
        while answer and answer[-1] < n and k > 0:      # 백준 2812 크게 만들기와 똑같음
            k -= 1
            answer.pop()
        answer.append(n)
    
    return ''.join(answer[0:len(number) - k])