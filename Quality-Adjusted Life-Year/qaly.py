years = int(input())
out = 0
for i in range(years):
    x = input().split()
    out += float(x[0])*float(x[1])

print(out)
