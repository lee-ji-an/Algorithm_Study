def solution(record):
    answer = []
    uid2Nickname = {}
    
    data = []
    for inst in map(lambda x: x.split(), record):
        op, uid = inst[0], inst[1]
        
        if (op == "Enter"):
            data.append((uid, "Enter"))
            uid2Nickname[uid] = inst[2]
        elif (op == "Leave"):
            data.append((uid, "Leave"))
            # del uid2Nickname[uid]
        elif (op == "Change"):
            uid2Nickname[inst[1]] = inst[2]
    
    for userId, op in data:
        res = f"{uid2Nickname.get(userId)}님이 {'들어왔' if op == 'Enter' else '나갔'}습니다."
        answer.append(res)
    
    return answer