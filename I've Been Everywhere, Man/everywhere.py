cases = int(input())
for i in range(cases):
    x = int(input())
    cities = []
    a = 0
    for s in range(x):
        city = input()
        if city not in cities:
            a+=1
            cities.append(city)
    print(a)
