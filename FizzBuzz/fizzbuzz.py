x = input().split()
x= [int(i) for i in x]
f = x[0]
b = x[1]
n = x[2]
for i in range(1,n+1):
    if i%f ==0 and i%b ==0:
        print("FizzBuzz")
    elif i%f == 0:
        print("Fizz")
    elif i%b == 0:
        print("Buzz")
    else:
        print(i)
