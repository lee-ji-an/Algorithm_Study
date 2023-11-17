from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    data = {k: defaultdict(int) for k in course}
    maxData = {k: {"value": 0, "detail": list()} for k in course}
    
    for order in orders:
        for menuCnt in course:
            for c in combinations(order, menuCnt):
                key = ''.join(sorted(c))
                data[menuCnt][key] += 1
                if (data[menuCnt][key] > maxData[menuCnt]["value"]):
                    maxData[menuCnt]["value"] = data[menuCnt][key]
                    maxData[menuCnt]["detail"] = [key]
                elif (data[menuCnt][key] == maxData[menuCnt]["value"]):
                    maxData[menuCnt]["detail"].append(key)
    
    tmp = []
    for k in course:
        if (maxData[k]["value"] > 1):
            for item in maxData[k]["detail"]:
                tmp.append(item)

    return sorted(tmp)
