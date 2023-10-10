x = input()
alive = False
dead = False
if ":)" in x:
    alive = True
if ":(" in x:
    dead = True

if alive and dead:
    print("double agent")
elif alive:
    print("alive")
elif dead:
    print("undead")
else:
    print("machine")

