x = []
y = []
for i in range(3):
    temp = input().split()
    x.append(int(temp[0]))
    y.append(int(temp[1]))
if x[0]==x[1]:
    x = x[2]
elif x[1]==x[2]:
    x = x[0]
else:
    x = x[1]
if y[0]==y[1]:
    y = y[2]
elif y[1]==y[2]:
    y = y[0]
else:
    y = y[1]

print(x,y)
