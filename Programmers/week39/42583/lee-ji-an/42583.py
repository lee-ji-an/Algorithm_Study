def solution(bridge_length, weight, truck_weights):
    from collections import deque

    bridge = deque()
    truck_waiting = deque(truck_weights)

    bridge_weight = 0
    time = 0

    # 큐에 가능한 최대 수의 트럭을 올림
    while truck_waiting and bridge_weight + truck_waiting[0] <= weight \
            and len(bridge) < bridge_length:
        time += 1
        w = truck_waiting.popleft()
        bridge.append((time, w))

        bridge_weight += w

    while bridge:
        # 트럭 한 대 빼기
        t, w = bridge.popleft()
        # (1) 트럭이 다리를 다 건너는 시간 vs (2) 현재 시간 비교했을 때
        # (1) 이 더 나중이면, 시간 갱신
        if bridge_length + t > time:
            time = bridge_length + t
        bridge_weight -= w

        # 다시 트럭 올리기
        while truck_waiting and bridge_weight + truck_waiting[0] <= weight \
                and len(bridge) < bridge_length:
            w = truck_waiting.popleft()
            bridge.append((time, w))

            bridge_weight += w
            time += 1

    return time
