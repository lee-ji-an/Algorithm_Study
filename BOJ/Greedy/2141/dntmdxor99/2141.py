n = int(input())
maps = []
sum_population = 0
for _ in range(n):
    town, population = map(int, input().split())
    maps.append([town, population])
    sum_population += population

half_population = sum_population // 2       # 절반을 넘어가면 거기가 최적?임
maps.sort(key = lambda x: x[0])

for town, population in maps:
    sum_population -= population
    if sum_population <= half_population:
        print(town)
        break
