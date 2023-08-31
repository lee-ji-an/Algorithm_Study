from collections import deque
import sys

N, K = map(int, sys.stdin.readline().strip().split())
N = list(map(int, list(str(N))))
M = len(N)
visited = [set() for _ in range(K+1)]  # 인덱스: 교환 횟수
candidate_max = -sys.maxsize

def swap(num_list: list[int], i, j):
    assert i < j
    
    # 바꾼 숫자가 0으로 시작하면 안됨
    if (i == 0 and num_list[j] == 0):
        return None
    
    num_list[i], num_list[j] = num_list[j], num_list[i]

    return num_list

q = deque()
q.append(N)
op_cnt = 1

while (q and op_cnt <= K):
    for _ in range(len(q)):
        cur_num = q.popleft()

        for i in range(M-1):
            for j in range(i+1, M):
                new_num = swap(cur_num.copy(), i, j)
                if (new_num is None):
                    continue
                # K번째 연산에 진입하면 최댓값 갱신
                if (op_cnt == K):
                    candidate_max = max(candidate_max, int(''.join(map(str, new_num))))

                if (str(new_num) in visited[op_cnt]):
                    continue
                visited[op_cnt].add(str(new_num))  # 연산 횟수별로 방문처리
                q.append(new_num)

    op_cnt += 1

print(candidate_max if candidate_max != -sys.maxsize else -1)
