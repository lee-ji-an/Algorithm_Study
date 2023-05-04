import sys
input = sys.stdin.readline


def long():
    maps = list(input().strip().split(':'))

    l = 8 - len(maps)       # ::의 개수를 세서 0000을 집어넣음
    match maps.count(''):
        case 1:
            # 1개만 있을 경우, 중간에 있다는 의미임
            maps[maps.index('')] = ('0' * 4 + ':') * l + '0000'
        case 2:
            # 2개가 있을 경우, 맨 앞 혹은 맨 뒤에 0000의 그룹이 있다는 의미임
            maps[maps.index('')] = ('0' * 4 + ':') * (l + 1) + '0000'
            maps.remove('')
    for i, num in enumerate(maps):
        if (l := len(num)) < 4:
            # 길이가 4보다 작으면 앞에 적은만큼 0을 추가해줌
            maps[i] = '0' * (4 - l) + num
    print(':'.join(maps))


def short():
    import ipaddress as _
    print(_.ip_address(input()).exploded)


if __name__ == "__main__":
    long()


