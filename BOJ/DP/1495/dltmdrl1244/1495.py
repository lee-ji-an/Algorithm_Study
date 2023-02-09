import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
delta = list(map(int, input().split()))
volumes = [s]

# 다음 번째에 연주 가능한 볼륨을 찾아 리턴
def find_next_volume(v, i):
    tmp = set()
    for cur in v:
        # 변화량 delta 만큼을 더하고 뺐을 때도 0 <= <= m 사이에 있다면 연주 가능한 볼륨
        if 0 <= cur + delta[i] <= m:
            tmp.add(cur + delta[i])
        if 0 <= cur - delta[i] <= m:
            tmp.add(cur - delta[i])

    return list(tmp)

# 시작 볼륨 s부터 시작하여 매번 다음 곡을 연주할 수 있는 볼륨을 volumes에 저장함
for i in range(n):
    volumes = find_next_volume(volumes, i)

# 마지막 volumes 배열이 비어있다면 연주할 수 없는 것이므로 -1
if volumes:
    print(max(volumes))
else:
    print(-1)