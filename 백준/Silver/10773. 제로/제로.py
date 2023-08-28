K = int(input())
nonZero = []
ans = 0

for i in range(K) :
    n = int(input())
    if n != 0 :
        ans += n
        nonZero.append(n)
    else :
        ans -= nonZero.pop()

print(ans)