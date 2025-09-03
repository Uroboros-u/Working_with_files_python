#Exercises 10-6
first_number = input('Write your first number: ')
second_number = input('Write your second number: ')

try:
    summ = int(first_number) + int(second_number)
except ValueError:
    print("You wrote not a number")
else:
    print("Summ: ", summ)