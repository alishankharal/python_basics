name = input("Enter your name: ")
while True:
    try:
        age = int(input("Enter your Age: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

field = input("Enter your Field: ")   
goal = input("Enter your Goal: ")  
print('-------STUDENT CARD-------')
print('Name:',name)
print('Age:',age)
print('Field:',field)
print('Goal:',goal)
print('---------------------------')
