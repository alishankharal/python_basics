name = input("Enter your name: ")

while True:
    try:
        rollNum = int(input("Enter your roll number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

while True:
    try:
        age = int(input("Enter your Age: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

city = input("Enter your City: ")   

print(f"\nAssalam o alaikum! I am {name}.")
print(f"My Roll Number is {rollNum}!")
print(f"Age is {age}!")
print(f"I belong from {city}!")