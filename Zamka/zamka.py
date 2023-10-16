l = int(input())
d = int(input())
x = int(input())
min = 0
max = 0
def sum(target):
    stringified = str(target)
    out = 0
    for i in range(len(stringified)):
        out=out + int(stringified[i])
    return out
    
for i in range(l-1,d+1):
    if sum(i) == x:
        min = i
        break

for i in reversed(range(l-1,d+1)):
    if sum(i) == x:
        max = i
        break
print(min)
print(max)
