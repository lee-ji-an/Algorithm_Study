from itertools import combinations
import sys

N, K = map(int, sys.stdin.readline().split())

# 모든 단어들은 anta~tica 형태이므로, K가 5 미만이면 아무 단어도 읽을 수 없음
if (K < 5):
    print(0)
    sys.exit()

words = []
# 각 문자열을 이진수 형태로 바꾸어 words에 저장
for _ in range(N):
    s = 0
    for ch in list(sys.stdin.readline().rstrip()):
        s |= (2**(ord(ch)-97))
    words.append(s)


# 'acint'를 제외한 모든 알파벳
comb = [2**i for i in range(26) if i not in (0, 2, 8, 13, 19)]

# K-5개의 알파벳을 조합하는 모든 경우를 탐색
result = 0
for c in combinations(comb, K-5):
    cnt = 0
    bit = 532741  # '0b10000010000100000101' -> 'acint' 의 기본 문자

    # 선택된 조합에 해당하는 알파벳들을 bit에 더해줌
    for i in c:
        bit += i

    # 현재 bit로 읽을 수 있는 단어의 개수를 구함
    # 2진수로 표현된 각 단어들과 현재 bit를 AND 연산했을 때, 변화가 없다면 모든 문자를 포함하는 것
    for word in words:
        if (bit & word == word):
            cnt += 1

    # 최댓값 업데이트
    result = max(cnt, result)

print(result)
