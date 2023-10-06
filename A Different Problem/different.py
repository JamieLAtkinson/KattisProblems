import sys
for line in sys.stdin:
    z=line.split()
    print(abs(int(z[0])-int(z[1])))
