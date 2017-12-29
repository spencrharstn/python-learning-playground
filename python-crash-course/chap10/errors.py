print("Enter two numbers to divide them.")
print("Enter 'q' to quit.")

while True:
    num1 = input("\nFirst number: ")
    if num1 == 'q':
        break
    num2 = input("Second number: ")
    if num2 == 'q':
        break
    try:
        answer = float(num1) / float(num2)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)