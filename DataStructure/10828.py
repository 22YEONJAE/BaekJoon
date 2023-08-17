# 스택 구현하기
# Silver 4

import sys
stack = []

def Push(n) :
    stack.append(n)

def Pop() :
    if Empty() == 1 :
        return -1
    else :
        return stack.pop()

def Size() :
    return len(stack)

def Empty() :
    if len(stack) == 0 :
        return 1
    else :
        return 0

def Top() :
    if Empty() == 1 :
        return -1
    else :
        return stack[-1]


num = int(input())

for i in range(num) :
    # strip은 sys.stdin.readline()을 할 때 뒤에 개행문자 삭제 !!
    # sys 를 쓰게되면 시간이 감소한다는 소문이..
    # 여러 줄을 입력 받을 때는 항상 sys 를 쓰자 !!
    command = sys.stdin.readline().strip().split(" ")

    if command[0] == "push" :
        Push(command[1])
    elif command[0] == "pop" :
        print(Pop())
    elif command[0] == "size" :
        print(Size())
    elif command[0] == "empty" :
        print(Empty())
    elif command[0] == "top" :
        print(Top())
