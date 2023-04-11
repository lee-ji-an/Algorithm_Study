import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split())) # 탑 높이
tower_count = [0] * (n)
nearest_tower = [float('inf')] * (n)

def solve(r):
    stack = []
    if r:
        for i in range(n-1, -1, -1):
            while stack and towers[stack[-1]] <= towers[i]:
                stack.pop()
            
            if len(stack):
                tower_count[i] += len(stack)
                
                if abs(nearest_tower[i] - i) > abs(stack[-1] - i):
                    nearest_tower[i] = stack[-1]
        
            stack.append(i)
    else:
        for i in range(n):
            while stack and towers[stack[-1]] <= towers[i]:
                stack.pop()
            
            if len(stack):
                tower_count[i] += len(stack)
                
                if abs(nearest_tower[i] - i) > abs(stack[-1] - i):
                    nearest_tower[i] = stack[-1]
        
            stack.append(i)


solve(False)
solve(True)

for i in range(n):
    if tower_count[i]:
        print(tower_count[i], nearest_tower[i] + 1)
    else:
        print(0)