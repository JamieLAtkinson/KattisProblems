x = int(input())
for i in range(x):
    td1 = input()
    td2 = input()
    out = ""
    for i in range(len(td1)):
        if td1[i]==td2[i]:
            out+="."
        else:
            out+="*"
    print(f"{td1}\n{td2}\n{out}\n")
