from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = sorted(Counter(tangerine).items(), key = lambda x : x[1], reverse = True)       # counter로 묶고, 정렬한다.
    while k > 0:        # k가 0 보다 작거나 같을 때까지 계속해서 과일을 추가한다. 당연하게도 갯수가 많은 애를 넣을수록 중복은 줄어든다.
        k -= count[answer][1]
        answer += 1
    
    return answer