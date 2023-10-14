x = input().split()
h = int(x[0])
m = int(x[1])
if m<45:
    h -=1
    if h<0:
        h = 23
    m = 60+m-45
else:
    m -=45
print(h,m)
