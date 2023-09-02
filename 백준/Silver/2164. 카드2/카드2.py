n = int(input())
cards = []
j = 0

for i in range(n) :
    cards.append(i+1)

for i in range(n-1) :
    j += 1
    cards.append(cards[j])
    j+=1

print(cards.pop())