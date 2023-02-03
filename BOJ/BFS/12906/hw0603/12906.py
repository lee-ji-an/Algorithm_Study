from collections import deque
import sys

visited = set()  # 방문 처리에 사용할 집합
dishmap = {'A': 1, 'B': 2, 'C': 3}  # 각 원판에 대응되는 비트(01, 10, 11)

# 입력 받음
initState = []
cntA, cntB, cntC = 0, 0, 0  # A, B, C  원판이 각각 몇 개씩 있는가?
for _ in range(3):
    line = sys.stdin.readline().split()
    bit = 0
    if (int(line[0])):
        cnt, dish = line
        for i in range(int(cnt)):
            bit |= (dishmap[dish[i]] << 2*i)
            match (dish[i]):
                case 'A': cntA += 1
                case 'B': cntB += 1
                case 'C': cntC += 1
    initState.append(bit)
initState = tuple(initState)

# 각 기둥에 같은 이름의 원판만 있을 때가 정답 튜플
make_answer_bit = lambda bitStr, dishCnt: int(f"0b{bitStr*dishCnt}", base=2) if dishCnt else 0
answerBit = (make_answer_bit('01', cntA), make_answer_bit('10', cntB), make_answer_bit('11', cntC))


def 비트를쪼개(bit: int) -> tuple[int, int]:
    """
    비트열을 하나 받아서, 맨 앞의 원판을 pop 하고, 원판에 해당하는 비트와 남은 비트열의 튜플을 반환
    A: 0b01, B: 0b10, C: 0b11
    이니까.. 비트열 길이가 홀수가 되는 경우가 생김(top 이 A인 경우). 이 때는 pop 동작 시 MSB하나만 뺴야 됨
    """
    if (bit.bit_length() % 2):
        bit = bit & ~(1 << bit.bit_length()-1)  # MSB 클리어
        return (dishmap["A"], bit)
    else:
        # MSB 두 자리를 봤을 때.. 10이면 B, 11이면 C
        # 근데 이 경우에는 MSB가 무조건 1이므로 MSB 다음 비트만
        MSB다음비트 = bit & (1 << bit.bit_length()-2)

        if (MSB다음비트):  # 11: C
            bit = bit & ~(1 << bit.bit_length()-1)  # MSB 2번 클리어
            bit = bit & ~(1 << bit.bit_length()-1)
            return (dishmap['C'], bit)
        else:  # 10: B
            bit = bit & ~(1 << bit.bit_length()-1)  # MSB 클리어
            return (dishmap['B'], bit)


def 맨앞에넣어(bit: int, top: int) -> int:
    """
    현재 기둥에 있는 원판 정보를 나타내는 비트열과, 그 위에 쌓을 원판 비트열 정보를 받아서 쌓은 비트열 반환
    """
    bit_len = bit.bit_length()
    # 'A'(01) 이라면 0 앞에 비트를 push 해야 하므로 한 칸 더 밀어줘야 함
    shift = bit_len + (1 if bit_len % 2 else 0)
    return bit | (top << shift)


def bfs() -> int:
    q = deque([initState])
    visited.add(initState)
    moveCnt = 0
    while (q):
        for _ in range(len(q)):
            a, b, c  = q.popleft()
            
            nextCandidate = []
            # A의 top을 B, C로 옮겨봄
            if (a):
                top, bitA = 비트를쪼개(a)
                bitB, bitC = 맨앞에넣어(b, top), 맨앞에넣어(c, top)  # A의 top을 B와 C의 top으로 옮긴 후의 비트열
                bitC = 맨앞에넣어(c, top)  # A의 top을 C의 top으로 옮긴 후 C의 비트열
                nextCandidate += [(bitA, bitB, c), (bitA, b, bitC)]  # 후보군 추가

            # B -> A | B-> C
            if (b):
                top, bitB = 비트를쪼개(b)
                bitA, bitC = 맨앞에넣어(a, top), 맨앞에넣어(c, top)
                nextCandidate += [(bitA, bitB, c), (a, bitB, bitC)]

            # C -> A | C -> B
            if (c):
                top, bitC = 비트를쪼개(c)
                bitA, bitB = 맨앞에넣어(a, top), 맨앞에넣어(b, top)
                nextCandidate += [(bitA, b, bitC), (a, bitB, bitC)]
            
            # 후보 튜플들을 순회하며 아직 방문하지 않은 노드들을 큐에 삽입
            for node in nextCandidate:
                if (node not in visited):
                    # 완료 상태에 도달했다면 움직인 횟수 반환
                    if (node == (answerBit)):
                        return moveCnt + 1
                    visited.add(node)
                    q.append(node)
        
        moveCnt += 1
        
    raise Exception("정답을 찾지 못함")

print(bfs() if answerBit != initState else 0)
