try:
    num = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print("invalid input")