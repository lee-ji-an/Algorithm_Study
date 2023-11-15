def solution(sequence, k):
    left, right, subTotal = 0, 0, sequence[0]
    leftCandidate, rightCandidate = 0, len(sequence)-1
    sequence.append(0)  # right 포인터가 sequence 밖으로 나가는 것 방지

    while (right < len(sequence)-1):
        if (subTotal <= k):
            if ((subTotal == k) and (right-left < rightCandidate-leftCandidate)):
                leftCandidate, rightCandidate = left, right
            right += 1
            subTotal += sequence[right]
        else:
            subTotal -= sequence[left]
            left += 1

    return [leftCandidate, rightCandidate]
