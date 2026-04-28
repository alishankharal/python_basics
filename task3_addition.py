while True:
    try:
        a=int(input('Enter your first number.'))
        break
    except ValueError:
        print('Invalid input!Enter again number as a input.')
while True:
    try:
        b=int(input('Enter your second number.'))
        break
    except ValueError:
        print('Invalid input!Enter again number as a input.')
sum=a+b
print(f"Sum of {a} and {b} is:{sum}")