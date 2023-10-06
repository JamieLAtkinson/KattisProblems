casenumber = input()
for i in range(int(casenumber)):
    solved = False
    target = int(input())
    for x in range(4):
        for y in range (4):
            for z in range(4):
                ans = f"4 {x} 4 {y} 4 {z} 4".replace("0","+").replace("1","-").replace("2","*").replace("3","//")
                total = int(eval(ans))
                if total == int(target) and solved == False:
                    print(ans.replace("//","/") + " = " + str(total))
                    solved=True
    if solved == False:
        print("no solution")
