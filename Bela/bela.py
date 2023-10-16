x = input().split()
dom = x[1]
dommap = {"A":11,"K":4,"Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}
basemap = {"A":11,"K":4,"Q":3,"J":2,"T":10,"9":0,"8":0,"7":0}
out = 0
for i in range(4*int(x[0])):
    y= input()
    if y[1] == dom:
        out+=dommap[y[0]]
    else:
        out+=basemap[y[0]]
print(out)
