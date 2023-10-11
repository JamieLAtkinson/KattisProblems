string = input()
out = ""
out = out + string[0]
for i in range(len(string)):
    if string[i] == "-":
        out= out + string[i+1]
print(out)
