x = input().split()
y= int(x[1])
for i in range(int(x[0])):
    y -= int(input())

if y >=0:
    print("Jebb")
else:
    print("Neibb")
