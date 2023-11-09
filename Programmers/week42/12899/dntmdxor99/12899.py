def solution(n):
    answer = ''
    convert = ['1', '2', '4']
    
    while n > 0:
        n -= 1      # 3진법이면 0, 1, 2인데, 이를 맞춰주기 위해 계속 1을 뺌
        answer = convert[n % 3] + answer
        n //= 3
    
    return answer