import sys
input = sys.stdin.readline


pri = {'A' : 0, 'a' : 1, 'B' : 2, 'b' : 3, 'C' : 4, 'c' : 5, 'D' : 6, 'd' : 7, 'E' : 8, 'e' : 9, 'F' : 10, 'f' : 11, 'G' : 12, 'g' : 13, 'H' : 14, 'h' : 15, 'I' : 16, 'i' : 17, 'J' : 18, 'j' : 19, 'K' : 20, 'k' : 21, 'L' : 22, 'l' : 23, 'M' : 24, 'm' : 25, 'N' : 26, 'n' : 27, 'O' : 28, 'o' : 29, 'P' : 30, 'p' : 31, 'Q' : 32, 'q' : 33, 'R' : 34, 'r' : 35, 'S' : 36, 's' : 37, 'T' : 38, 't' : 39, 'U' : 40, 'u' : 41, 'V' : 42, 'v' : 43, 'W' : 44, 'w' : 45, 'X' : 46, 'x' : 47, 'Y' : 48, 'y' : 49, 'Z' : 50, 'z' : 51}


def int_merge(item):
    i = 0
    l = len(item)
    while i < l:
        if item[i].isdigit():
            right = i + 1
            while right < l and item[right].isdigit():
                right += 1
            item[i : right] = [''.join(item[i : right])]
            l = len(item)
        i += 1

    return item


def compare(x, y):      # y의 우선 순위가 높으면 True를 반환함
    l = min(len(x), len(y))
    for i in range(l):
        itx = x[i]
        ity = y[i]
        if itx.isalpha():
            if ity.isalpha():
                if pri[itx] > pri[ity]:
                    return True
                elif pri[itx] < pri[ity]:
                    return False
                else:
                    continue
            else:
                return True
        else:
            if y[i].isalpha():
                return False
            else:
                if int(itx) != int(ity):
                    itx, ity = int(itx), int(ity)
                    if itx < ity:
                        return False
                    elif itx > ity:
                        return True
                    else:
                        continue
                else:
                    return False if len(itx) < len(ity) else True


def quick_sort(maps, left, right):
    if left >= right:
        return

    mid = partition(maps, left, right)

    quick_sort(maps, left, mid - 1)
    quick_sort(maps, mid, right)

    return maps


def partition(maps, left, right):
    pivot = maps[(left + right) // 2]
    mid = (left + right) // 2

    while left <= right:
        while not compare(maps[left], pivot):       # False라면 pivot보다 우선순위가 높음. 따라서 True일 떄만 증가시키면 됨
            left += 1

        while compare(maps[right], pivot):      # False라면 pivot보다 우선순위가 높음. True라면 pivot보다 우선순위가 낮음. 따라서 pivot보다 우선 순위가 높은 애를 찾아야 함
            right -= 1

        if left <= right:
            maps[left], maps[right] = maps[right], maps[left]
            left, right = left + 1, right - 1

    if left < mid:
        maps[left], maps[mid] = maps[mid], maps[left]
        left = mid
    elif right > mid:
        maps[right], maps[mid] = maps[mid], maps[right]

    return left


if __name__ == "__main__":
    n = int(input())
    maps = list(map(int_merge, [list(input().strip()) for _ in range(n)]))

    # print(*maps, sep='\n')

    # for i in range(n):
    #     for j in range(i, n):
    #         if compare(maps[i], maps[j]):       # True라면 교환
    #             maps[i], maps[j] = maps[j], maps[i]

    maps = quick_sort(maps, 0, n - 1)

    for i in maps:
        print(''.join(i))

