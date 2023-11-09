def solution(cards):
    def dfs(n):
        score = 0
        while cards[n]:
            score += 1
            temp = cards[n]
            cards[n] = 0
            n = temp - 1
            
        return score
    
    
    score = []
    for i in range(len(cards)):
        if cards[i]:
            score.append(dfs(i))
    
    score.sort(reverse = True)

    if len(score) > 1:
        return score[0] * score[1]
    else:
        return 0