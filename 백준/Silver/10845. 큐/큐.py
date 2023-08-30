import sys

N = int(input())
Qu = []

def PUSH(n) :
    Qu.append(n)

def EMPTY() :
    if len(Qu) == 0 :
        return 1
    else :
        return 0

def POP() :
    if EMPTY() :
        return -1
    return Qu.pop(0)

def SIZE() :
    return len(Qu)

def FRONT() :
    if EMPTY() :
        return -1
    return Qu[0]

def BACK() :
    if EMPTY() :
        return -1
    return Qu[SIZE()-1]

for i in range(N) :
    inst = sys.stdin.readline().strip().split(" ")
    
    if inst[0] == "push" :
        PUSH(inst[1])
    elif inst[0] == "pop" :
        print(POP())
    elif inst[0] == "size" :
        print(SIZE())
    elif inst[0] == "empty" :
        print(EMPTY())
    elif inst[0] == "front" :
        print(FRONT())
    elif inst[0] == "back" :
        print(BACK())
