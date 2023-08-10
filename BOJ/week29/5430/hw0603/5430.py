import sys

T = int(sys.stdin.readline())


for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = eval(sys.stdin.readline())

    isReversed = False
    left, right = 0, len(arr)  # [left, right)

    for op in p:
        match (op):
            case 'R':  # 뒤집기
                isReversed = True ^ isReversed
            case 'D':  # 첫 원소 버리기
                if (left == right):
                    print("error")
                    break
                if (isReversed):
                    right -= 1
                else:
                    left += 1
    else:
        answerArr = list(reversed(arr[left:right])) if isReversed else arr[left:right]
        print(str(answerArr).replace(' ', ''))
