import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maps = []
    pc = [0] * (n + 1)
    for _ in range(n):
        heapq.heappush(maps, list(map(int, input().split())))

    end_time = []
    can_use = [*range(n)]       # 자리의 리스트

    while maps:
        s, e = heapq.heappop(maps)
        while end_time and s > end_time[0][0]:      # 현재 시작 시간보다 빨리 끝나는 자리가 있다면 모두 pop 함
            _, idx = heapq.heappop(end_time)
            heapq.heappush(can_use, idx)        # 앉을 수 있는 자리의 리스트에 넣음
        index = heapq.heappop(can_use)
        heapq.heappush(end_time, [e, index])        # 끝나는 시간 리스트에 넣음
        pc[index] += 1

    for i in range(n + 1):
        if pc[i] == 0:
            print(i)
            print(*pc[:i], sep=' ')
            break
