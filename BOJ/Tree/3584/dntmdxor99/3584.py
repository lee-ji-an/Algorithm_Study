import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    par = dict()
    my_par = set()
    for _ in range(T):
        par.clear()
        my_par.clear()
        N = int(input())
        for _ in range(N - 1):
            A, B = map(int, input().split())
            par[B] = A      # B의 부모는 A임
        a, b = map(int, input().split())

        while True:
            # A의 부모를 루트 노드까지 찾음
            if a not in par:
                my_par.add(a)
                break
            my_par.add(a)
            a = par[a]

        if b in my_par:
            # 만약 거기에 b가 속해있다면 출력 후 종료
            print(b)
            continue

        while True:
            # a와 b의 공통된 조상을 찾음
            if b in my_par:
                print(b)
                break
            b = par[b]