alphabet = {
    "a":"@",
    "b":"8",
    "c":"(",
    "d":"|)",
    "e":"3",
    "f":"#",
    "g":"6",
    "h":"[-]",
    "i":"|",
    "j":"_|",
    "k":"|<",
    "l":"1",
    "m":"[]\/[]",
    "n":"[]\[]",
    "o":"0",
    "p":"|D",
    "q":"(,)",
    "r":"|Z",
    "s":"$",
    "t":"']['",
    "u":"|_|",
    "v":"\/",
    "w":"\/\/",
    "x":"}{",
    "y":"`/",
    "z":"2"
}

text = input().strip().lower()
output = ""
for i in text:
    try:
        output = output+alphabet[i]
    except:
        output = output+i
print(output)
