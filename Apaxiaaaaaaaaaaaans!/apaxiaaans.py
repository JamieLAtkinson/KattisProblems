name = input()
out = ""
curlet = ""
for i in range(len(name)):
    if name[i] != curlet:
        out += name[i]
        curlet = name[i]

print(out)
