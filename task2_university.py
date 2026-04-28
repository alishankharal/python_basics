name = input("Enter your name:")
university = input("Enter your university name:")
depart = input("Enter your department:")

while True:
    try:
        semester = int(input("Enter your semester: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

   

print(f"\nMy Name:{name}.")
print(f"University:{university}!")
print(f"Department: {depart}!")
print(f"Current Semester {semester}th")