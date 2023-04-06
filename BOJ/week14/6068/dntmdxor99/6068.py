import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    maps = sorted(maps, key = lambda x : x[1], reverse = True)      # 뒤에서부터 넣어봄

    now = float('inf')
    for t, e in maps:
        now = min(now, e) - t       # 현재 시간과 끝내야 하는 시간에서 최소를 구한 후에 차근차근히 넣어봄
    print(now if now >= 0 else -1)      # 만약 넣지 못하는 상황이 생긴다면 now가 음수가 됨
