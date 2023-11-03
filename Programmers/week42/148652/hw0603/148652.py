from collections import defaultdict

def solution(cards):
    """
    그룹으로 나누고, 각 그룹 중 젤큰거 두개 골라서 크기 곱 반환
    """
    
    groupData = defaultdict(set)
    cards = [None] + cards
    
    idx = 1
    groupIdx = 0
    visited = set()
    currentVal = cards[idx]
    while (len(visited)+1 < len(cards)):
        if (currentVal not in groupData[groupIdx]):
            groupData[groupIdx].add(currentVal)
            visited.add(currentVal)
            currentVal = cards[currentVal]
        else:
            # 사이클 만났을 때
            groupIdx += 1
            for i in range(1, len(cards)):
                if (cards[i] in visited):
                    continue
                currentVal = cards[i]
                break
    
    if (len(groupData) <= 1):
        return 0
    
    group_sizes = sorted(len(group) for group in groupData.values())
    
    return group_sizes[-1] * group_sizes[-2]
    