raw_string = input()
length = len(raw_string)
new_string = ""
for i in range(length):
    new_string = new_string + raw_string[length-1-i]
    
print(new_string)
    
