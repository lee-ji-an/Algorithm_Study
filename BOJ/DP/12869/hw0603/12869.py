from itertools import permutations
from collections import deque
import sys

N = int(sys.stdin.readline())
hp = tuple(map(int, sys.stdin.readline().split()))
visited = set()

q = deque([hp])
cnt = 0
while (q):
    for _ in range(len(q)):
        node = q.popleft()

        if (len(node) == 3):
            for a, b, c in permutations(range(3), 3):
                newnode = [None, None, None]
                if ((zero := node[a]-9) > 0):
                    newnode[a] = zero
                if ((one := node[b]-3) > 0):
                    newnode[b] = one
                if ((two := node[c]-1) > 0):
                    newnode[c] = two
                
                newnode = tuple([i for i in newnode if i])
                if not any(newnode):
                    print(cnt+1)
                    sys.exit()
                if newnode in visited:
                    continue
                q.append(newnode)
                visited.add(newnode)

        elif (len(node) == 2):
            for a, b in ((0, 1), (1, 0)):
                newnode = [None, None, None]
                if ((zero := node[a]-9) > 0):
                    newnode[a] = zero
                if ((one := node[b]-3) > 0):
                    newnode[b] = one
                
                newnode = tuple([i for i in newnode if i])
                if not any(newnode):
                    print(cnt+1)
                    sys.exit()
                if (newnode in visited):
                    continue
                q.append(newnode)
                visited.add(newnode)

        else:
            newnode = node[0]-9
            if (newnode > 0):
                if ((newnode,) not in visited):
                    q.append((newnode,))
                    visited.add((newnode,))
            else:
                print(cnt+1)
                sys.exit()

    cnt += 1
