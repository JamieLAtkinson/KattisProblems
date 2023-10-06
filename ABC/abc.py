number = input().split()
numbers = [eval(i) for i in number]
order = input()
maxno = max(numbers)
numbers.remove(maxno)
minno = min(numbers)
numbers.remove(minno)
middleno = numbers[0]

order = order[0]+" "+order[1]+" "+order[2]
print(order.replace("A",str(minno)).replace("B",str(middleno)).replace("C",str(maxno)))
