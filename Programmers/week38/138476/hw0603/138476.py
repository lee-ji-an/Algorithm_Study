from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    sortedkeys = sorted(counter.keys(), key=lambda x: counter.get(x), reverse=True)

    answer = 0
    cnt = 0
    for idx, key in enumerate(sortedkeys):
        cnt += counter.get(key)
        if (cnt >= k):
            answer = idx+1
            break

    return answer
