#Exercises 10-7
while True:
    print("This is a simple calculator. You can add two numbers.")
    print("Write 'q' if you want to exit.")

    first_number = input('Write your first number: ')
    if first_number == 'q':
        break
    second_number = input('Write your second number: ')
    if second_number == 'q':
        break

    try:
        summ = int(first_number) + int(second_number)
    except ValueError:
        print("You wrote not a number. Please try again!\n")
    else:
        print("Summ: ", summ, '\n')