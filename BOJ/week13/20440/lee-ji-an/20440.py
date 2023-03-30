import heapq
import sys
input = sys.stdin.readline

N = int(input())

hq = []
visited = [False] * N

for i in range(N):
    start, end = map(int, input().split())
    heapq.heappush(hq, (start, i))
    heapq.heappush(hq, (end, i))


def solve():
    max_cnt, cnt = 0, 0
    start, end = 0, 0
    prev = -1
    flag = False
    for i in range(N * 2):
        time, m_num = heapq.heappop(hq)
        if visited[m_num]:  # 입장시간일 때
            cnt -= 1
            if flag:
                end = time
                flag = False
        else:  # 퇴장일 때
            cnt += 1
            visited[m_num] = True
            if max_cnt == cnt and prev == time:  # 최댓값의 구간이 끝나자마자 새로 시작할 때
                flag = True
            if max_cnt < cnt:
                max_cnt = cnt
                start = time
                flag = True  # 최댓값이 갱신되었다는 표시
        prev = time

    return max_cnt, start, end


max_cnt, em, xm = solve()
print(max_cnt)
print(em, xm)
