import sys
input = sys.stdin.readline

"""
 _____                                         __                              
/\  __`\                                      /\ \__    __                     
\ \ \/\ \    __  __     __     ___      ____  \ \ ,_\  /\_\     ___     ___    
 \ \ \ \ \  /\ \/\ \  /'__`\ /' _ `\   /',__\  \ \ \/  \/\ \   / __`\ /' _ `\  
  \ \ \\'\\ \ \ \_\ \/\  __/ /\ \/\ \ /\__, `\  \ \ \_  \ \ \ /\ \L\ \/\ \/\ \ 
   \ \___\_\ \ \____/\ \____\\ \_\ \_\\/\____/   \ \__\  \ \_\\ \____/\ \_\ \_\
    \/__//_/  \/___/  \/____/ \/_/\/_/ \/___/     \/__/   \/_/ \/___/  \/_/\/_/
                                                                               
                                                                               """

if __name__ == "__main__":
    n, c = map(int, input().split())
    maps = []
    for _ in range(n):
        maps.append(int(input()))

    maps.sort()

    start, end = 1, maps[-1] - maps[0]      # 최소 거리와 최대 거리
    ans = 0

    if c == 2:
        print(end)
    elif c == n:
        print(min([maps[i + 1] - maps[i] for i in range(n - 1)]))
    else:
        while start < end:
            mid = (start + end) // 2        # mid 거리 이상만큼 공유기를 설치함

            cnt = 1
            bef = maps[0]

            for i in range(n):
                if maps[i] - bef >= mid:
                    cnt += 1
                    bef = maps[i]

            ## 아래 주석까지의 부분이 잘 이해가 안 감
            if cnt >= c:
                ans = mid
                start = mid + 1
            elif cnt < c:
                end = mid
            ##

        print(ans)
