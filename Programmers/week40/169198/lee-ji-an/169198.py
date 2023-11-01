def solution(m, n, startX, startY, balls):
    import math
    answer = []

    for ball in balls:
        score = float('inf')
        targetX, targetY = ball[0], ball[1]

        # left
        rateA, rateB = startX / (startX + targetX), targetX / (startX + targetX)
        lenA, lenB = abs(startY - targetY) * rateA, abs(startY - targetY) * rateB
        if not (lenA == 0 and lenB == 0 and (targetX < startX)):
            score = min(score, (math.sqrt(lenA ** 2 + startX ** 2) + math.sqrt(lenB ** 2 + targetX ** 2)) ** 2)

        # top
        rateA, rateB = (n - startY) / (n - startY + n - targetY), (n - targetY) / (n - startY + n - targetY)
        lenA, lenB = abs(startX - targetX) * rateA, abs(startX - targetX) * rateB
        if not (lenA == 0 and lenB == 0 and (targetY > startY)):
            score = min(score,
                        (math.sqrt(lenA ** 2 + (n - startY) ** 2) + math.sqrt(lenB ** 2 + (n - targetY) ** 2)) ** 2)

        # right
        rateA, rateB = (m - startX) / (m - startX + m - targetX), (m - targetX) / (m - startX + m - targetX)
        lenA, lenB = abs(startY - targetY) * rateA, abs(startY - targetY) * rateB

        if not (lenA == 0 and lenB == 0 and (targetX > startX)):
            score = min(score,
                        (math.sqrt(lenA ** 2 + (m - startX) ** 2) + math.sqrt(lenB ** 2 + (m - targetX) ** 2)) ** 2)

        # bottom
        rateA, rateB = startY / (startY + targetY), targetY / (startY + targetY)
        lenA, lenB = abs(startX - targetX) * rateA, abs(startX - targetX) * rateB

        if not (lenA == 0 and lenB == 0 and targetY < startY):
            score = min(score, (math.sqrt(lenA ** 2 + startY ** 2) + math.sqrt(lenB ** 2 + + targetY ** 2)) ** 2)

        answer.append(round(score))

    return answer
