metadata = input()
potionNo = int(metadata.split()[0])
time = int(metadata.split()[1])

potions = []

for i in range (potionNo):
    potions.append(int(input()))
potions.sort(reverse=True)

for i in range(potionNo):
    for x in potions[0:i]:
        potions[i] = x - time
    
if min(potions)>0:
    print("YES")
else:
    print("NO")
