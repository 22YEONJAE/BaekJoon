# 수 찾기

import sys

N = int(input())

# list의 Search 는 O(n)
# map 의 Search 는 O(1)
A = set(map(int,sys.stdin.readline().split()))

M = int(input())

B = list(map(int, sys.stdin.readline().split()))

for i in B :
    # 리스트에 특정 원소가 몇개 있는지 체크 !
    if i in A :
        print(1)
    else :
        print(0)