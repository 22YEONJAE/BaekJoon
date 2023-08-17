# 수 정렬하기2
# 정렬
# sort() -> 오름차순 정렬
# sort(reverse = TRUE) 내림차순 정렬
#
# sys 정리
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
# 여러 줄 입력받을 때 아주 편함, 한 줄 + /n (개행문자) 까지 저장하기 때문에 형변환 필요
# strip()은 문자열 맨 앞과 맨 끝의 공백문자를 제거합니다.

import sys

n = int(input())
n_list = []

for i in range(n) :
    n_list.append(int(sys.stdin.readline()))


n_list.sort()

for i in n_list :
    print(i)