x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))

if x%3 == 0 and y%3 == 0 and z%3 == 0:
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    elif z > x and z > y:
        print(z)
else:
    print('none of them are odd')