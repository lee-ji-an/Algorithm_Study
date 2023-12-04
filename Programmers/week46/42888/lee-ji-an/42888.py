def solution(record):
    answer = []
    user = {}
    command_record = []
    for rec in record:
        command = rec.split()
        # 채팅방 입장
        if command[0].startswith("E"):
            user[command[1]] = command[2]
            command_record.append(("E", command[1]))
        # 채팅방 퇴장
        elif command[0].startswith("L"):
            command_record.append(("L", command[1]))
        # 닉네임 변경
        else:
            user[command[1]] = command[2]

    for action, userId in command_record:
        if action == 'E':
            answer.append(user[userId] + "님이 들어왔습니다.")
        else:
            answer.append(user[userId] + "님이 나갔습니다.")

    return answer
