# 괄호
# 괄호 문자열 
# Silver 4

num = int(input())
PS = []

# list 에 string 집어넣기 (여러줄에 걸쳐 받는 경우 !!)
for i in range(num) :
    PS.append(input())

for i in PS :
    if len(i) % 2 == 1 :
        print("NO")
    else :
        cnt = 0

        for j in range(len(i)) :
            if i[j] == "(" :
                cnt += 1
            else :
                cnt -= 1
            # ) 가 ( 보다 먼저 나와버린 경우!
            if cnt < 0 :
                print("NO")
                break
        

        if cnt == 0 :
            print("YES")
        elif cnt > 0 :
            print("NO")
