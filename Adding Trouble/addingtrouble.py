x = input().split()
y = [eval(i) for i in x]
if y[0]+y[1]==y[2]:
    print("correct!")
else:
    print("wrong!")
