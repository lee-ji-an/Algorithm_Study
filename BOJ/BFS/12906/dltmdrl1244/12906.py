from collections import deque

asum, bsum, csum = 0, 0, 0

def ids(a):
    if a == 'A':
        return 1
    elif a == 'B':
        return 11
    else:
        return 111
# 입력 받는 부분. 숫자가 0일 수도 있다.
A = input()
if A != '0':
    ac = int(A.split()[0])
    al = list(A.split()[1])
    for i in range(ac):
        asum += ids(al[i])
else:
    ac = int(A.split()[0])
    al = []

B = input()
if B != '0':
    bc = int(B.split()[0])
    bl = list(B.split()[1])
    for i in range(bc):
        bsum += ids(bl[i])
else:
    bc = int(B.split()[0])
    bl = []

C = input()
if C != '0':
    cc = int(C.split()[0])
    cl = list(C.split()[1])
    for i in range(cc):
        if cl[i] == 'A':
            csum += 1
        elif cl[i] == 'B':
            csum += 11
        else:
            csum += 111
else:
    cc = int(C.split()[0])
    cl = []

# set에 집어넣기 위해 튜플로 만들어 줌
def tuplize(a, b, c):
    return tuple([tuple(a), tuple(b), tuple(c)])


def copy(a):
    return a[:]

# 종료조건
def check(a, b, c):
    return ('B' not in a and 'C' not in a) and ('A' not in b and 'C' not in b) and ('A' not in c and 'B' not in c)



def bfs(a, b, c):
    q = deque()
    q.append((copy(a), copy(b), copy(c), asum, bsum, csum))
    v = set()
    v.add(tuplize(a, b, c))
    cnt = 0
    while q:
        # 큐 길이만큼만 반복함으로써 cnt를 전역으로 조절함
        for _ in range(len(q)):
            ca, cb, cc, casum, cbsum, ccsum = q.popleft()

            if check(ca, cb, cc):
                return cnt

            # 자기 막대기에 속하지 않는 원판이 있으면 다른 두 곳으로 옮겨본다.
            # 자기 막대기에 속하는 원판만 있으면 옮기면 안된다.
            if casum >= 11:
            # if 'B' in ca or 'C' in ca: 이렇게 해도 됨
                t1 = tuplize(ca[:-1], cb + [ca[-1]], cc)
                t2 = tuplize(ca[:-1], cb, cc + [ca[-1]])
                t = ids(ca[-1])
                # v(set)에 없다면, 즉 탐색하지 않았던 새로운 조합이라면 큐에 넣는다.
                if t1 not in v:
                    v.add(t1)
                    q.append((copy(ca[:-1]), copy(cb + [ca[-1]]), copy(cc), casum - t, cbsum + t, ccsum))

                if t2 not in v:
                    v.add(t2)
                    q.append((copy(ca[:-1]), copy(cb), copy(cc + [ca[-1]]), casum - t, cbsum, ccsum + t))

            if cbsum != 0 and (cbsum < 11 or cbsum >= 111 or cbsum % 11 != 0):
                t1 = tuplize(ca + [cb[-1]], cb[:-1], cc)
                t2 = tuplize(ca, cb[:-1], cc + [cb[-1]])
                t = ids(cb[-1])

                if t1 not in v:
                    v.add(t1)
                    q.append((copy(ca + [cb[-1]]), copy(cb[:-1]), copy(cc), casum + t, cbsum - t, ccsum))

                if t2 not in v:
                    v.add(t2)
                    q.append((copy(ca), copy(cb[:-1]), copy(cc + [cb[-1]]), casum, cbsum - t, ccsum + t))

            if ccsum != 0 and (ccsum < 111 or ccsum % 111 != 0):
                t1 = tuplize(ca + [cc[-1]], cb, cc[:-1])
                t2 = tuplize(ca, cb + [cc[-1]], cc[:-1])
                t = ids(cc[-1])

                if t1 not in v:
                    v.add(t1)
                    q.append((copy(ca + [cc[-1]]), copy(cb), copy(cc[:-1]), casum + t, cbsum, ccsum - t))

                if t2 not in v:
                    v.add(t2)
                    q.append((copy(ca), copy(cb + [cc[-1]]), copy(cc[:-1]), casum, cbsum + t, ccsum - t))

        cnt += 1

print(bfs(al, bl, cl))