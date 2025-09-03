from pathlib import Path

path = Path('pi_million_digits.txt')
data = path.read_text()

lines = data.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

birthday = input('Write your birthday (expample: 02.02.2020): ')
birthday = birthday.replace('.', '')

if birthday in pi_string:
    print('Your birthday is in Pi!')
else:
    print('Your birthday is NOT in Pi!')
