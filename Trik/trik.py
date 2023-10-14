left = 1
middle = 0
right = 0
moves = input().lower()
for i in range(len(moves)):
    move = moves[i]
    if move == "a":
        temp = left
        left = middle
        middle = temp
    elif move == "b":
        temp = middle
        middle = right
        right = temp
    else:
        temp = right
        right = left
        left = temp
if left ==1:
    print("1")
elif middle == 1:
    print("2")
else:
    print("3")
