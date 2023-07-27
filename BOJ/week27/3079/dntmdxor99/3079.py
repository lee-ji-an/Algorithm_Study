import sys
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    maps = [int(input()) for _ in range(n)]

    start, end = min(maps) * (m // n), max(maps) * (m // n + 1)     # 최솟값은 무조건 불가능한 것, 최댓값은 무조건 가능한 것으로 설정해야 함 -> 질문 게시판 데이터 추가 요청

    """
    2 3
    9
    10
    
    정답 : 18

    데이터가 들어오면 최소 9초에서 20초로 설정해야 하는데, end를 max(maps) * (m // n)으로 해버리면 9~10초 사이만 탐색함
    """
    
    while start <= end:
        mid = (start + end) // 2        # 해당 mid 시간 안에 끝낼 수 있나를 확인하면 됨

        cnt = 0
        for i in range(n):
            cnt += mid // maps[i]       # 각 심사대에서 해당 시간 안에 받을 수 있는 최대 인원
            
        if cnt >= m:        # 수용 가능한 인원이 m보다 많거나 같음
            end = mid - 1
        else:
            start = mid + 1

    print(end + 1)


if __name__ == "__main__":
    sol()
