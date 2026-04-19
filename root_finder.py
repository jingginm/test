#Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6
#and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message
#to that effect.

integer = int(input('Enter an integer: '))
root = int(1)
pwr = int(0)

while root <= integer:
    pwr = 1
    while pwr <= 6:
        if root**pwr == integer:
            print(f'pwr: {pwr}, root: {root}')
        pwr = pwr + 1
    root = root + 1
