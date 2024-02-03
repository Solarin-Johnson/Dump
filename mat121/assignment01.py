# import time
def factorial(x):
    if x == 0 or x ==1:
        return 1
    else:
        return x * factorial(x-1)
    
while True:
    userInput = input("Enter a number to calculate its factorial: ")
    # time.sleep(0.2)
    try:
        number = int(userInput)
        if number >= 0:
            result = factorial(number)
            print(f'The Factorial of the number {userInput} is {result} \n')
        else:
            print('Please enter a positive integer \n')
    except ValueError:
        print('Invalid Input, Please Enter a Valid Number \n')
        # time.sleep(0.5)
    anotherNumber = input("Do you want to want to find the factorial of another number? (y/n): ")
    if anotherNumber.lower() != 'y':
        break
    # time.sleep(0.2)