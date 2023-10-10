input()
x = input().split()
c = 0
for i in x:
    if int(i)<0:
        c+=1
        
print(c)
