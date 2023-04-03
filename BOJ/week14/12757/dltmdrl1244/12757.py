import sys
input = sys.stdin.readline

class LLRB:      
    class Node:                
        def __init__(self, key, val): # Constructor
            self.key, self.val = key, val
            self.left = self.right = None
            self.count = 1 # Number of nodes itself and below            
            self.red = True # Color of parent link

    def __init__(self): # Constructor
        self.root = None

    @staticmethod
    def getOnNode(h, key):
        while h != None:
            if key < h.key: h = h.left
            elif key > h.key: h = h.right
            else: return h.val # key == x.key
        return None # The key was NOT found

    def get(self, key):
        return LLRB.getOnNode(self.root, key)

    def contains(self, key):
        return self.get(key) != None

    @staticmethod    
    def isRed(x):
            if x == None: return False
            return x.red

    @staticmethod 
    def fixUp(h): # Fix the tree such that it conforms to the LLRB representation
        if h == None: return None
        if LLRB.isRed(h.right) and not LLRB.isRed(h.left): h = LLRB.rotateLeft(h)  # Lean right -> lean left
        if LLRB.isRed(h.left) and LLRB.isRed(h.left.left): h = LLRB.rotateRight(h) # 4-node all leaning left -> 4-node leaning left and right
        if LLRB.isRed(h.left) and LLRB.isRed(h.right): LLRB.flipColors(h) # Split a 4-node into two 2-nodes
        return h
    
    @staticmethod 
    def rotateLeft(h):
        assert(LLRB.isRed(h.right))
        x = h.right
        h.right = x.left
        x.left = h
        x.red = h.red
        h.red = True
        return x

    @staticmethod
    def rotateRight(h):
        assert(LLRB.isRed(h.left))
        x = h.left
        h.left = x.right
        x.right = h
        x.red = h.red
        h.red = True
        return x

    @staticmethod
    def moveRedLeft(h):
        LLRB.flipColors(h)
        if LLRB.isRed(h.right.left):
            h.right = LLRB.rotateRight(h.right)
            h = LLRB.rotateLeft(h)
            LLRB.flipColors(h)
        return h
    
    @staticmethod
    def moveRedRight(h):
        LLRB.flipColors(h)
        if LLRB.isRed(h.left.left):
            h = LLRB.rotateRight(h)
            LLRB.flipColors(h)
        return h

    @staticmethod
    def flipColors(h):
        #assert((not LLRB.isRed(h) and LLRB.isRed(h.left) and LLRB.isRed(h.right)) or\
        #    (LLRB.isRed(h) and not LLRB.isRed(h.left) and not LLRB.isRed(h.right)))        
        h.red = not h.red
        h.left.red = not h.left.red
        h.right.red = not h.right.red
        
    def put(self, key, val):
        def putOnNode(x, key, val):
            if x == None: return self.Node(key, val)
            if key < x.key: x.left = putOnNode(x.left, key, val)
            elif key > x.key: x.right = putOnNode(x.right, key, val)
            else: x.val = val # key == x.key
            x = LLRB.fixUp(x)
            return x     
        self.root = putOnNode(self.root, key, val)
        self.root.red = False # To not violate the assertion in flipColors(h), where the root splits


    def floor(self, key, k):
        def floorOnNode(x, key):
            if x == None: return None
            if key == x.key: return x
            elif key < x.key: return floorOnNode(x.left, key)

            t = floorOnNode(x.right, key)
            if t != None: return t
            else: return x
        x = floorOnNode(self.root, key)
        if x == None or abs(key - x.key) > k: return None
        else: return x.key

    def ceiling(self, key, k):
        def ceilingOnNode(x, key):
            if x == None: return None
            if key == x.key: return x
            elif x.key < key: return ceilingOnNode(x.right, key)

            t = ceilingOnNode(x.left, key)
            if t != None: return t
            else: return x
        x = ceilingOnNode(self.root, key)
        if x == None or abs(key - x.key) > k: return None
        else: return x.key

bst = LLRB()
n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    t = list(map(int, input().split()))
    bst.put(t[0], t[1])

for _ in range(m):
    command = list(map(int, input().split()))
    if command[0] == 1: # 값 삽입
        bst.put(command[1], command[2])

    elif command[0] == 2: # 값 수정
        if bst.get(command[1]): # 정확한 키 값 있음
            bst.put(command[1], command[2])

        else:
            floor = bst.floor(command[1], k)
            ceiling = bst.ceiling(command[1], k)
            
            if not floor and ceiling:
                bst.put(ceiling, command[2])
            elif floor and not ceiling:
                bst.put(floor, command[2])
            elif floor and ceiling:
                a = abs(floor - command[1])
                b = abs(ceiling - command[1])
                if a > b:
                    bst.put(ceiling, command[2])
                elif a < b:
                    bst.put(floor, command[2])

    else:
        if bst.get(command[1]):
            print(bst.get(command[1]))
        else:
            floor = bst.floor(command[1], k)
            ceiling = bst.ceiling(command[1], k)
            if not floor and ceiling:
                print(bst.get(ceiling))
            elif floor and not ceiling:
                print(bst.get(floor))
            elif not floor and not ceiling:
                print(-1)
            else:
                a = abs(floor - command[1])
                b = abs(ceiling - command[1])
                if a == b:
                    print('?')
                elif a < b:
                    print(bst.get(floor))
                else:
                    print(bst.get(ceiling))