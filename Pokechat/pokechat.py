key = input()
raw_data = input()
data = [raw_data[i:i+3] for i in range(0,len(raw_data),3)]
out = ""
for i in data:
    out = out + key[int(i)-1]
print(out)
